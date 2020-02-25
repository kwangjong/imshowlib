#library for showing numpy images on jupyter notebook
#
#   to use imshow3d, after import do:
#       %matplotlib inline
#
# - imshow2d: show 2d image
# - imshow2dAll: imshow2d multiple images using subplots
# - imshow3d: show 3d image by slices across axis=2 (zs)
# - gridshow3d: show 3d projection of image
# - gridshow3d: gridshow3d for multiple images using subplots

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
from ipywidgets import interact

#show 2D images
def imshow2d(img, grid=False, mask=None, alpha=0.4, 
             xticks=[], yticks=[], label=None, 
             fontsize=None, cmap=None, figsize=None, figsave=None):
    if mask is not None and len(mask.shape) is 2:
        alpha_layer = mask*alpha
        mask = np.stack((np.zeros(mask.shape), mask, mask, alpha_layer), axis=2)
    
    fig = None
    if figsize is None:
        fig = plt.figure()
    else:
        fig = plt.figure(figsize=figsize)

    plt.grid(grid)
    
    if xticks is not None:
        plt.xticks(xticks)
        
    if yticks is not None:
        plt.yticks(yticks)
    
    if label is not None:
        if fontsize is not None:
            plt.xlabel(label, fontsize=fontsize)
        else:
            plt.xlabel(label)
        
    plt.imshow(img, cmap=cmap)
    if(mask is not None):
            plt.imshow(mask)
            
    plt.show()
    if figsave is not None:
        fig.savefig(figsave)

#show 2D images
#dim dimension of table
#    images will be shown from left right corner to row-column order
def imshow2dAll(imgs, dim, grid=False, mask=None, alpha=0.4,
             xticks=[], yticks=[], label=None, 
             fontsize=None, cmap=None, figsize=None, figsave=None):
    
    fig = None
    if figsize is None:
        fig = plt.figure()
    else:
        fig = plt.figure(figsize=figsize)
        

    for i in range(len(imgs)):
        
        if imgs[i] is None:
            continue
        
        if mask is not None and mask[i] is not None and len(mask[i].shape) is 2:
            alpha_layer = mask[i]*alpha
            mask[i] = np.stack((np.zeros(mask[i].shape), mask[i], mask[i], alpha_layer), axis=2)
        
        if isinstance(grid, bool):
            plt.grid(grid)
        else:
            plt.grid(grid[i])
        
        plt.subplot(dim[0], dim[1], i+1)
        
        if xticks is not None:
            if len(xticks) is not len(imgs):
                plt.xticks(xticks)
            else:
                plt.xticks(xticks[i])

        if yticks is not None:
            if len(xticks) is not len(imgs):
                plt.yticks(yticks)
            else:
                plt.yticks(yticks[i])

        if label is not None:
            if fontsize is not None:
                plt.xlabel(label[i], fontsize=fontsize)
            else:
                plt.xlabel(label[i])
        if cmap is not None and type(cmap) is matplotlib.colors.LinearSegmentedColormap:
            plt.imshow(imgs[i], cmap=cmap)
        elif cmap is not None:
            plt.imshow(imgs[i], cmap=[i])
        else:
            plt.imshow(imgs[i])
        if mask is not None and mask[i] is not None:
                plt.imshow(mask[i])
    plt.show()
    if figsave is not None:
        fig.savefig(figsave)        

#show 3D image as slices
def imshow3d(img, grid=False, mask=None, alpha=0.4, 
             xticks=[], yticks=[], label=None, 
             fontsize=None, cmap=None, figsize=None, continuous_update=True):
    min_layer = 0
    max_layer = img.shape[2]-1
    if mask is not None:
        alpha_layer = mask*alpha
        mask = np.stack((np.zeros(mask.shape), mask, mask, alpha_layer), axis=3)
    
    def update(z):
        if mask is None:
            imshow2d(img[:,:,z], grid=grid, 
                     xticks=xticks, yticks=yticks, label=label, 
                     fontsize=fontsize, cmap=cmap, figsize=figsize)
        else:
            imshow2d(img[:,:,z], grid=grid, mask=mask[:,:,z,:],
                     xticks=xticks, yticks=yticks, label=label, 
                     fontsize=fontsize, cmap=cmap, figsize=figsize)
            
    interact(update, z=widgets.IntSlider(value=0, min=min_layer, max=max_layer, step=1, continuous_update=continuous_update))

#plot three-dimensional object in 3D grid space
def gridshow3d(img, label=None, fontsize=None, 
               cmap=None, figsize=None, figsave=None):
    
    xs =[]
    ys =[]
    zs=[]
    clrs =[]

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if(img[i][j][k] > 0):
                    xs.append(i)
                    ys.append(j)
                    zs.append(k)
                    clrs.append(img[i][j][k])

    xs = np.array(xs)
    ys = np.array(ys)
    zs = np.array(zs)
    clrs = np.array(clrs)

    fig = None
    if figsize is None:
        fig = plt.figure()
    else:
        fig = plt.figure(figsize=figsize)
    
    ax = fig.gca(projection='3d')  
    ax.set_xlim(0,img.shape[0])
    ax.set_ylim(0,img.shape[1])
    ax.set_zlim(0,img.shape[2])
    
    
    if label is not None:
        if fontsize is not None:
            ax.set_title(label, y=-0.2, fontsize=fontsize)
        else:
            ax.set_title(label, y=-0.2)
            
    ax.scatter(xs,
               ys,
               zs,
               c=clrs, cmap=cmap)
    
    fig.tight_layout()
    fig.show()
    if figsave is not None:
        fig.savefig(figsave)
        
#plot mutiple images of three-dimensional objects in 3D grid spaces
def gridshow3dAll(imgs, dim, label=None, fontsize=None, 
                  cmap=None, figsize=None, figsave=None, label_offset=-0.01):
    
    fig = None
    if figsize is None:
        fig = plt.figure()
    else:
        fig = plt.figure(figsize=figsize)
    
    for i in range(len(imgs)):
        
        if imgs[i] is None:
            continue
        
        plot = imgs[i]
        
        xs =[]
        ys =[]
        zs=[]
        clrs =[]

        for x in range(len(plot)):
            for y in range(len(plot[x])):
                for z in range(len(plot[x][y])):
                    if(plot[x][y][z] > 0):
                        xs.append(x)
                        ys.append(y)
                        zs.append(z)
                        clrs.append(plot[x][y][z])

        xs = np.array(xs)
        ys = np.array(ys)
        zs = np.array(zs)
        clrs = np.array(clrs)
        
        
        ax = fig.add_subplot(dim[0], dim[1], i+1, projection='3d')
        ax.set_xlim(0,plot.shape[0])
        ax.set_ylim(0,plot.shape[1])
        ax.set_zlim(0,plot.shape[2])
        
        if label is not None:
            if fontsize is not None:
                ax.set_title(label[i], y=label_offset, fontsize=fontsize)
            else:
                ax.set_title(label[i], y=label_offset, fontsize=fontsize)
        
        if cmap is not None and type(cmap) is matplotlib.colors.LinearSegmentedColormap:
            ax.scatter(xs,
                       ys,
                       zs,
                       c=clrs, cmap=cmap)
        elif cmap is not None:
            ax.scatter(xs,
                       ys,
                       zs,
                       c=clrs, cmap=cmap[i])
        else:
            ax.scatter(xs,
                       ys,
                       zs,
                       c=clrs, cmap=cmap)
    
    fig.tight_layout()
    fig.show()
    if figsave is not None:
        fig.savefig(figsave)
