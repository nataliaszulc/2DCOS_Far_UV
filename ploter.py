import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.gridspec import GridSpec

def combine_plots(spec_syn, spec_asyn, base_file):
    base = pandas.read_excel(base_file, header=0, index_col=0,usecols=[0,1])
    base = base[base.columns[0]]
    fig = plt.figure(figsize=(15.5,6)) #15.5,6
    fig.text(0.13, 0.8, 'A', fontsize = 16, c='0')
    fig.text(0.56, 0.8, 'B', fontsize = 16, c='0')
    gs = GridSpec(nrows=2, ncols=9, width_ratios=[1,.5,5,.5,1.5,1,.5,5,.5], height_ratios=[1,5])
    ax_s_map = fig.add_subplot(gs[1,2])
    ax_s_x = fig.add_subplot(gs[0,2])
    ax_s_y = fig.add_subplot(gs[1,0])
    s_colorbar = fig.add_subplot(gs[1,3])  
    #annotate_s = fig.add_axes(gs[0,0])
    ax_a_map = fig.add_subplot(gs[1,7])
    ax_a_x = fig.add_subplot(gs[0,7])
    ax_a_y = fig.add_subplot(gs[1,5])
    a_colorbar = fig.add_subplot(gs[1,8])
  
    x, y, z, zmax = coords(spec_syn)
  
    z_max = z.max()
    z_min = z.min()  
    print(z_min, z_max)
  
    ind_max = numpy.unravel_index(numpy.argmax(spec_syn, axis=None), spec_syn.shape)
    xy_max = (spec_syn.columns[ind_max[0]], spec_syn.columns[ind_max[1]])
    ax_s_map.annotate(xy_max, xy=xy_max, xycoords='data', xytext=(xy_max[0]+5,xy_max[1]+5), bbox=dict(boxstyle="round", alpha=0.5, facecolor='white',ec="none"), arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
  
    ind_min = numpy.unravel_index(numpy.argmin(spec_syn, axis=None), spec_syn.shape)
    xy_min = (spec_syn.columns[ind_min[0]],spec_syn.columns[ind_min[1]])
    if xy_min[0]==xy_max[0]:
        xy_min_position = (xy_min[0] + 4, xy_min[1])
    elif xy_min[1]==xy_max[1]:
        xy_min_position = (xy_min[0], xy_min[1] + 4)
    else:
      xy_min_position = xy_min
      
    ax_s_map.annotate(xy_min, xy=xy_min, xycoords='data',xytext=(xy_min_position[0]+5,xy_min_position[1]+5), bbox=dict(boxstyle="round", alpha=0.5, facecolor='white',ec="none"), arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
    ax_s_x.plot(x, base, c='0')
    ax_s_x.tick_params(labelsize=9)
    ax_s_x.set_xlim(min(x), max(x))
    ax_s_x.set_ylim(min(base), max(base))
    ax_s_x.set_ylabel(r'$\theta$', labelpad=1)
    ax_s_y.plot(base,x, c='0')
    ax_s_y.tick_params(labelsize=9)
    ax_s_y.set_xlim(max(base), min(base))
    ax_s_y.set_ylim(min(x), max(x))
    ax_s_y.set_xlabel(r'$\theta$', labelpad=1)
    pcm_s = ax_s_map.pcolormesh(x,y,z,cmap='jet',vmin=-1*zmax,vmax=zmax,shading='gouraud')
    ax_s_map.add_artist(lines.Line2D(x,y,linewidth=.5,c='0'))
    fig.colorbar(pcm_s,cax=s_colorbar,label='Energy values').ax.tick_params(labelsize=9)
    s_colorbar.set_ylim(z_min, z_max)
  
    ax_s_map.contour(x,y,z,5,colors='0', linewidths=.5)
    ax_s_map.set_xlim(min(x), max(x))
    ax_s_map.set_ylim(min(y), max(y))
    ax_s_map.set_xlabel(r'$\lambda$ (nm)', labelpad=1)
    ax_s_map.set_ylabel(r'$\lambda$ (nm)', labelpad=1)
 
    #ASYNCHRONOUS
    x, y, z, zmax = coords(spec_asyn)
  
    ind_max = numpy.unravel_index(numpy.argmax(spec_asyn, axis=None), spec_asyn.shape)
    xy_max = (spec_asyn.columns[ind_max[0]], spec_asyn.columns[ind_max[1]])
    ax_a_map.annotate(xy_max, xy=xy_max, xycoords='data', xytext=(xy_max[0]+5,xy_max[1]+5), bbox=dict(boxstyle="round", alpha=0.5, facecolor='white',ec="none"), arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))

    ind_min = numpy.unravel_index(numpy.argmin(spec_asyn, axis=None), spec_asyn.shape)
    xy_min = (spec_asyn.columns[ind_min[0]], spec_asyn.columns[ind_min[1]])
    if xy_min[0]==xy_max[0]:
        xy_min_position = (xy_min[0] + 4, xy_min[1])
    elif xy_min[1]==xy_max[1]:
        xy_min_position = (xy_min[0], xy_min[1] + 4)
    else:
        xy_min_position = xy_min
    ax_a_map.annotate(xy_min, xy=xy_min_position, xycoords='data',xytext=(xy_min_position[0]+5,xy_min_position[1]+5), bbox=dict(boxstyle="round", alpha=0.5, facecolor='white',ec="none"), arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
  
    ax_a_x.plot(x, base, c='0')
    ax_a_x.tick_params(labelsize=9)
    ax_a_x.set_xlim(min(x), max(x))
    ax_a_x.set_ylim(min(base), max(base))
    ax_a_x.set_ylabel(r'$\theta$', labelpad=1)
    ax_a_y.plot(base,x, c='0')
    ax_a_y.tick_params(labelsize=9)
    ax_a_y.set_xlim(max(base), min(base))
    ax_a_y.set_ylim(min(x), max(x))
    ax_a_y.set_xlabel(r'$\theta$', labelpad=1)
    pcm_a = ax_a_map.pcolormesh(x,y,z,cmap='jet',vmin=-1*zmax,vmax=zmax,shading='gouraud')
    ax_a_map.add_artist(lines.Line2D(x,y,linewidth=.5,c='0'))
    fig.colorbar(pcm_a,cax=a_colorbar,label='Energy values').ax.tick_params(labelsize=9)
    ax_a_map.contour(x,y,z,5,colors='0', linewidths=.5)
    ax_a_map.set_xlim(min(x), max(x))
    ax_a_map.set_ylim(min(y), max(y))
    ax_a_map.set_xlabel(r'$\lambda$ (nm)', labelpad=1)
    ax_a_map.set_ylabel(r'$\lambda$ (nm)', labelpad=1)
  
    fig.suptitle(base_file[5:-4], y=.95, fontsize=16)
  
    plt.savefig(('results/Sample ' + base_file[5:-4] +' 2D-COS.png'), dpi=300, bbox_inches='tight')
    plt.show()

def coords(spec):
    x = spec.columns[0:].astype(float)
    y = spec.index[0:].astype(float)
    z = spec.values
    zmax = numpy.absolute(z).max()
    return x,y,z,zmax
