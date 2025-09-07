
# Output of your model
Please use the same [input](https://github.com/open-mmlab/mmclassification/blob/master/docs/dataset.md#id51) as [model](#id7), then run `python tools/dist_train.py configs/retinanet/retinanet_r101_fpn_2x_coco.py` on your model, and use `python tools/dist_test.py <config file path> <model checkpoint file name>.pth` to evaluate the model.

## Note
If you can not install dependencies using [these installation guides](https://mmclassification.readthedocs.io/en/latest/build.html#installation), please try again by installing them manually.

