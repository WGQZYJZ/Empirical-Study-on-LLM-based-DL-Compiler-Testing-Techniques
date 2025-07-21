'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
_input_tensor = torch.randn(4, 5)
_output_tensor = torch.Tensor.narrow_copy(_input_tensor, 1, 1, 2)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)