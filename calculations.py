import math
import numpy
import pandas

def correlation(inputfile1):
  spec1 = pandas.read_excel(inputfile1, header=0, index_col=0).T
  spec2 = spec1.copy()
  spec1 = spec1 - spec1.mean()
  spec2 = spec2 - spec2.mean()

  # Synchronous correlation
  sync = pandas.DataFrame(spec1.values.T @ spec2.values / (len(spec1) - 1))
  sync.index = spec1.columns
  sync.columns = spec2.columns
  sync = sync.T
  # Contourplot(sync)
  sync.to_csv('results/' + inputfile1[5: len(inputfile1) - 4] + '_sync.csv')
  
  # Hilbert-Noda transformation matrix
  noda = numpy.zeros((len(spec1), len(spec1)))
  for i in range(len(spec1)):
      for j in range(len(spec1)):
          if i != j: noda[i, j] = 1 / math.pi / (j - i)
  
  # Asynchronouse correlation
  asyn = pandas.DataFrame(spec1.values.T @ noda @ spec2.values / (len(spec1) - 1))
  asyn.index = spec1.columns
  asyn.columns = spec2.columns
  asyn = asyn.T
  # Contourplot(asyn)
  asyn.to_csv('results/' + inputfile1[5: len(inputfile1) - 4] + "_async.csv")

  return sync, asyn
