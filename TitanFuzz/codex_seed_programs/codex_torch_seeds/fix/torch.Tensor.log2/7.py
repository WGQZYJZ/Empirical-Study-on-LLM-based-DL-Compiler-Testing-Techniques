'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input Tensor: ', _input_tensor)
_output_tensor = torch.Tensor.log2(_input_tensor)
print('Output Tensor: ', _output_tensor)