'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
_input_tensor = torch.randn(3, 4)
_output_tensor = torch.Tensor.transpose(_input_tensor, 0, 1)
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _output_tensor)