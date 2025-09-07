Please note that in order to convert a tensor into `float` type with the specified dtype, please use [convert_element_type](https://pytorch.org/docs/stable/generated/torch.nn.functional.convert_element_type.html#torch.nn.functional.convert_element_type) API.


# Example of model running and inference
The first input is generated from the following tensor:
The second input to the model should be generated from the following matrix, where all the elements are `0`:
Please note that in order to fill a tensor with the specified values using `torch.full`, please use [torch.zeros](https://pytorch.org/docs/stable/generated/torch.zeros.html) API instead of [torch.full](https://pytorch.org/docs/stable/generated/torch.nn.functional.full.html).


# Test data
A tensor with a shape `N, H, W` and values of type `float32` will be used to train the model. The input tensor is initialized with [randn](https://pytorch.org/docs/stable/generated/torch.randn.html) API to generate random values. For each row in the input tensor, a tensor with a shape `[H, W]` and values of type `float32` will be generated using [uniform_(-0.5, 0.5), uniform_(-0.5, 0.5)] for the channels number to be converted from float type to float64. A tensor with `C` elements will be created by multiplying the input tensor and [tensor](https://pytorch.org/docs/stable/generated/torch.tensor.html) operation to generate random values, where each element in the resulting tensor is `[0, 1]`. Finally, a sum of all elements of the output tensor is created using [torch.sum](https://pytorch.org/docs/stable/generated/torch.sum.html). Please note that if you set `dtype` to be `float32`, the size and shape of the input tensor should not exceed 32-bit limit of [int32](https://docs.scipy.org/doc/numpy/reference/generated/numpy.int32.html).


# Input shape
The first argument for the model should be a single tensor, where each element is `[C, H, W]`, where `N` represents the batch size and `C` represents the channels number, and other attributes are same as that tensor. It also accepts a list of tensors as input. Please note that when a single input to the model is passed instead of list of inputs, it expects a shape `[batch_size, C, H, W]`, where all the attributes are same as that input.


# Output shape
A single tensor with `C` elements will be generated, where each element in the resulting tensor is `[H, W]` and the corresponding attribute will be filled with the values specified in [torch.arange](https://pytorch.org/docs/stable/generated/torch.arange.html) API.


# Additional Notes
None
