# Imshowlib

A library for viewing medical images on jupyter notebook. Voxel image array should be coverted to a numpy array. 3D image MxNxK (MxN images with K slices) can be displayed by slice using imshowlib.imshow3d(). 

### Prerequisites

* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)

### Usage
```
import imshowlib as imshow
```
to use imshow3d, after import do:
```
%matplotlib inline
```


## Documentation
* [imshow2d](#imshow2d)
* [imshow3d](#imshow3d)
* [gridshow3d](#gridshow3d)
* [imshow2dAll](#imshow2dAll)
* [gridshow3dAll](#gridshow3dAll)


## imshow2d
display 2d image array
```
imshowlib.imshow2d(img, grid=False, mask=None, alpha=0.4, xticks=[], yticks=[], label=None, 
fontsize=None, cmap=None, figsize=None, figsave=None)
```
#### parameters:
| Name          | Type                              | Description                                                      |
| ------------- | --------------------------------- | ---------------------------------------------------------------- |
| img           | array-like or PIL image           | image data; supported shapes are (M, N), (M, N, 3), or (M, N, 4) |
| grid          | bool, optional                    | whether to show grid line                                        |
| mask          | array-like or PIL image, optional | mask to overlay on top of image. data should be two-dim binary   |
| alpha         | scalar, optional                  | The alpha value of the mask                                      |
| xticks        | array_like, optional              | list of positions at which ticks should be placed                |
| yticks        | array_like, optional              | list of positions at which ticks should be placed                |
| label         | str, optional                     | label text                                                       |
| fontsize      | scalar, optional                  | font size of label                                               |
| cmap          | str or Colormap, optional         | Colormap used to map scalar data to colors                       |
| figsize       | (float, float), optional          | width, height in inches                                          |
| figsave       | str, optional                     | save path and format                                             |


## imshow2dAll
display multiple 2d image arrays with pyplot.subplot
```
imshowlib.imshow2dAll(imgs, dim, grid=False, mask=None, alpha=0.4, xticks=[], yticks=[], label=None, 
fontsize=None, cmap=None, figsize=None, figsave=None)
```
#### parameters:
| Name          | Type                                 | Description                                                      |
| ------------- | ------------------------------------ | ---------------------------------------------------------------- |
| img           | (array-like or PIL image,)           | list of image data; supported shapes are (M, N), (M, N, 3), or (M, N, 4) |
| dim           | (integer, integer)                   | number of rows and column of subplots. plots will be displayed from top-left corner |
| grid          | (bool,), optional                    | whether to show grid line                                        |
| mask          | (array-like or PIL image,), optional | mask to overlay on top of image. data should be two-dim binary   |
| alpha         | (scalar,), optional                  | The alpha value of the mask                                      |
| xticks        | (array_like,), optional              | list of positions at which ticks should be placed                |
| yticks        | (array_like,), optional              | list of positions at which ticks should be placed                |
| label         | (str,), optional                     | label text                                                       |
| fontsize      | (scalar,), optional                  | font size of label                                               |
| cmap          | (str or Colormap,), optional         | Colormap used to map scalar data to colors                       |
| figsize       | (float, float), optional             | width, height in inches                                          |
| figsave       | str, optional                        | save path and format                                             |


## imshow3d
display 3d image arrays as slices along axis=2
use interactive slider to scroll through slices
```
imshowlib.imshow3d(img, grid=False, mask=None, alpha=0.4, xticks=[], yticks=[], label=None, 
fontsize=None, cmap=None, figsize=None, continuous_update=True)
```
#### parameters:
| Name              | Type                              | Description                                                      |
| ----------------- | --------------------------------- | ---------------------------------------------------------------- |
| img               | ndarray                           | image data; supported shapes are (M, N, K)                       |
| grid              | bool, optional                    | whether to show grid line                                        |
| mask              | ndarray, optional                 | mask to overlay on top of image. data should be three-dim binary |
| alpha             | scalar, optional                  | The alpha value of the mask                                      |
| xticks            | array_like, optional              | list of positions at which ticks should be placed                |
| yticks            | array_like, optional              | list of positions at which ticks should be placed                |
| label             | str, optional                     | label text                                                       |
| fontsize          | scalar, optional                  | font size of label                                               |
| cmap              | str or Colormap, optional         | Colormap used to map scalar data to colors                       |
| figsize           | (float, float), optional          | width, height in inches                                          |
| figsave           | str, optional                     | save path and format                                             |
| continuous_update | bool, optional                    | if true, continuously update image when scrolling                |



## gridshow3d
```
imshowlib.gridshow3d(img, label=None, fontsize=None, cmap=None, figsize=None, figsave=None)
```
#### parameters:
| Name              | Type                              | Description                                                      |
| ----------------- | --------------------------------- | ---------------------------------------------------------------- |
| img               | ndarray                           | volumetric data; supported shapes are (M, N, K)                  |
| label             | str, optional                     | label text                                                       |
| fontsize          | scalar, optional                  | font size of label                                               |
| cmap              | str or Colormap, optional         | Colormap used to map scalar data to colors                       |
| figsize           | (float, float), optional          | width, height in inches                                          |
| figsave           | str, optional                     | save path and format                                             |

## gridshow3dAll
```
imshowlib.gridshow3dAll(imgs, dim, label=None, fontsize=None, cmap=None, figsize=None, figsave=None, 
label_offset=-0.01)
```
#### parameters:
| Name              | Type                              | Description                                                      |
| ----------------- | --------------------------------- | ---------------------------------------------------------------- |
| img               | (ndarray,)                        | array or list of volumetric data; supported shapes are ((M, N, K),)                  |
| label             | (str,), optional                  | list of label texts                                               |
| fontsize          | (scalar,), optional               | list of font sizes of label                                       |
| cmap              | (str,) or Colormap, optional      | list of Colormaps used to map each plot's scalar data to colors   |
| figsize           | (float, float), optional          | width, height in inches                                          |
| figsave           | str, optional                     | save path and format                                             |
