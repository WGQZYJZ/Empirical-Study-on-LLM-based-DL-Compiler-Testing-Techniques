'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
_input_tensor = torch.rand(4, 4)
_output_tensor = torch.Tensor.as_strided(_input_tensor, (2, 2), (2, 2))
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)