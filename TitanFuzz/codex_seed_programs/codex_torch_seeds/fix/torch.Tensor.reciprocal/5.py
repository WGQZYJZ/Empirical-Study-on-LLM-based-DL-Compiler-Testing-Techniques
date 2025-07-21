'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.reciprocal(_input_tensor)
print('The reciprocal of input tensor is: ', _output_tensor)