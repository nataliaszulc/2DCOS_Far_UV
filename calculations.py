import math
import numpy
import pandas

def correlation(inputfile1):
  spec1 = pandas.read_excel(inputfile1, header=0, index_col=0).T
  spec2 = spec1.copy()
  #inputfile2 = inputfile1
  #spec2 = pandas.read_csv(inputfile2, header=0, index_col=0).T
  #spec1.T.plot(legend=None)
  #pyplot.show()
  """if left_large: plt.xlim(max(spec1.columns), min(spec1.columns))
  if hetero:
      spec2.T.plot(legend=None)
      if left_large:
          plt.xlim(max(spec2.columns), min(spec2.columns))
          plt.show()"""
  #If dynamic:
  spec1 = spec1 - spec1.mean()
  spec2 = spec2 - spec2.mean()
  """
  def contourplot(spec):
      x = spec.columns[0:].astype(float)
      y = spec.index[0:].astype(float)
      z = spec.values
      zmax = numpy.absolute(z).max()
      plt.figure(figsize=(6, 6))
      plt.contour(x, y, z, num_contour, cmap="bwr", vmin=-1 * zmax, vmax=zmax)
      plt.pcolormesh(x,y,z,cmap='jet',vmin=-1*zmax,vmax=zmax,shading='gouraud')
      if left_large:
          plt.xlim(max(x), min(x))
          plt.ylim(max(y), min(y))
      plt.show()"""
    
  # synchronous correlation
  sync = pandas.DataFrame(spec1.values.T @ spec2.values / (len(spec1) - 1))
  sync.index = spec1.columns
  sync.columns = spec2.columns
  sync = sync.T
  #contourplot(sync)
  sync.to_csv('results/' + inputfile1[5: len(inputfile1) - 4] + '_sync.csv')
  
  # Hilbert-Noda transformation matrix
  noda = numpy.zeros((len(spec1), len(spec1)))
  for i in range(len(spec1)):
      for j in range(len(spec1)):
          if i != j: noda[i, j] = 1 / math.pi / (j - i)
  
  # asynchronouse correlation
  asyn = pandas.DataFrame(spec1.values.T @ noda @ spec2.values / (len(spec1) - 1))
  asyn.index = spec1.columns
  asyn.columns = spec2.columns
  asyn = asyn.T
  #contourplot(asyn)
  asyn.to_csv('results/' + inputfile1[5: len(inputfile1) - 4] + "_async.csv")

  return sync, asyn