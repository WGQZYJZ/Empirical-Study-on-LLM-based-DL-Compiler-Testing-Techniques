'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
import torch
_input_tensor = torch.arange(1, 5, dtype=torch.float32)
print('Input tensor:', _input_tensor)
print('Output tensor:', _input_tensor.tile((2, 2)))
print('Output tensor:', _input_tensor.tile((1, 2)))
print('Output tensor:', _input_tensor.tile((2, 1)))
print('Output tensor:', _input_tensor.tile((2, 3)))
print('Output tensor:', _input_tensor.tile((3, 2)))
print('Output tensor:', _input_tensor.tile((2, 2, 2)))
print('Output tensor:', _input_tensor.tile((1, 2, 2)))
print('Output tensor:', _input_tensor.tile((2, 1, 2)))
print