# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where a convolution layer is followed by a batch normalization layer. The output of the convolution layer is used as the input to the batch normalization layer. 

The `fuse_conv_bn` optimization is triggered when the convolution and batch normalization layers are in evaluation mode (not in training mode), and the batch normalization layer is tracking running statistics. 

After the optimization, the convolution and batch normalization layers are fused into a single convolution layer, and the batch normalization layer is removed from the graph. If the output of the convolution layer is used by other nodes, the optimization will not be performed. 
