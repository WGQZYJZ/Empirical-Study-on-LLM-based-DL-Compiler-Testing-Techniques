'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(size=(1, 3, 224, 224))
_output_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)