'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
import torch
_input_tensor = torch.arange(1, 21).view(4, 5)
print('Input tensor: \n', _input_tensor)
_output_tensor = torch.Tensor.as_strided(_input_tensor, (3, 4), (5, 1))
print('Output tensor: \n', _output_tensor)
'\nExpected output:\nInput tensor:\n tensor([[ 1,  2,  3,  4,  5],\n        [ 6,  7,  8,  9, 10],\n        [11, 12, 13, 14, 15],\n        [16, 17, 18, 19, 20]])\nOutput tensor:\n tensor([[ 1,  2,  3,  4],\n        [ 6,  7,  8,  9],\n        [11, 12, 13, 14]])\n'