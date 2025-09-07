This pattern characterizes scenarios where a convolution and batch normalization layers are combined into a single layer by fusion, and the batch normalization layer is removed from the graph. If the output of the convolution is used by other nodes, the optimization will not be performed.

