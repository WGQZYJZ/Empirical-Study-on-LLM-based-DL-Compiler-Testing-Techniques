The `fuse_conv_bn` optimization is triggered when the batch normalization layer has not been fused to a convolution layer and the input tensor is smaller than 4 dimensions (not in training mode).

