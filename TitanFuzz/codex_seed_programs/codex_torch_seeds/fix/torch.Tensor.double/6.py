'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(10, 10)
_output_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _output_tensor)