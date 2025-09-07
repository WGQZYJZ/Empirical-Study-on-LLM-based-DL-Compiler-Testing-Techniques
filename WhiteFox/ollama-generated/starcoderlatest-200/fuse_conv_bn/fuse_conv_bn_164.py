The `fuse_bn_conv` optimization is triggered when the batch normalization layer (or equivalent API function) and convolution layer are in evaluation mode (not in training mode), and the batch normalization layer is tracking running statistics. 

After the optimization, the batch normalization layer or functional API equivalent of it is fused into a single batch normalization layer or functional API equivalent of it, and the convolution layer and batch normalization layer are removed from the graph. If any output tensor is used by other nodes, the optimization will not be performed. 

The optimization also applies to the functional API equivalent of the above pattern, where `torch.nn.functional.batch_norm` and `torch.nn.functional.conv2d` are used instead of the module API. The constraints for the functional API pattern are similar to the module API pattern.


# Description of requirements
The model should contain a series of convolutions and batch normalization layers followed by linear transformation, such as:
In each iteration of the loop, a convolutional layer is replaced by a batch normalization layer.
This pattern characterizes scenarios where a convolution is followed by multiple instances of a same batch norm operation. This scenario can be extended to a depthwise convolution for efficiency (depthwise conv has similar computation complexity with conv, but requires less GPU memory). 

In addition to the above pattern, there are also patterns such as:
This pattern characterizes scenarios where a batch norm is followed by another batch norm or a single linear function applied on the output of batch normalization layer. 

The `fuse_bn_batchnorm` optimization applies to above scenarios.

