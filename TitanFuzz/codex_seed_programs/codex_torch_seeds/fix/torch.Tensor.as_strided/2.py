'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
_input_tensor = torch.arange(0, 9, dtype=torch.float32).reshape(3, 3)
print('Input Tensor: ', _input_tensor)
_output_tensor = torch.Tensor.as_strided(_input_tensor, size=(2, 2), stride=(3, 3))
print('Output Tensor: ', _output_tensor)