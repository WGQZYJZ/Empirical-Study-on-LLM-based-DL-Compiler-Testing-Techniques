# Input type
Each tensor has a different datatype. It is recommended to use `torch.Tensor` to represent all inputs of model.

The data type that models a `PyTorch API` depends on the number of dimensions, shape of input_tensor and output_tensor. For example, the shape of the input tensor for a Conv2d or a MaxPool2d depends on the spatial dimension, and the number of channels is the last dimension (X = 3).
