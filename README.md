# imshowlib

Library for showing numpy images on jupyter notebook.

### Prerequisites

* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)

### Usage
```
import imshowlib as imshow
```
To use imshow3d, after import do:
```
%matplotlib inline
```
or
```
%matplotlib notebook
```
### Documentation
* [imshow2d](#imshow2d)
* [imshow3d](#imshow3d)
* [gridshow3d](#gridshow3d)
* [imshow2dAll](#imshow2dAll)
* [gridshow3dAll](#gridshow3dAll)


#### imshow2d
```
imshow2d(img, grid=False, mask=None, alpha=0.4, 
          xticks=[], yticks=[], label=None, fontsize=None, 
          cmap=None, figsize=None, figsave=None)
```


#### imshow2dAll
```
imshow2dAll(imgs, dim, grid=False, mask=None, alpha=0.4,
             xticks=[], yticks=[], label=None, fontsize=None, 
             cmap=None, figsize=None, figsave=None)
```

#### imshow3d
```
imshow3d(img, grid=False, mask=None, alpha=0.4, 
          xticks=[], yticks=[], label=None, fontsize=None, 
          cmap=None, figsize=None, continuous_update=True)
```

#### gridshow3d
```
gridshow3d(img, label=None, fontsize=None, 
            cmap=None, figsize=None, figsave=None)
```

#### gridshow3dAll
```
gridshow3dAll(imgs, dim, label=None, fontsize=None, 
               cmap=None, figsize=None, figsave=None, label_offset=-0.01)
```
