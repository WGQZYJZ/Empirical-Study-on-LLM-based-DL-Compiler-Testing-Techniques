'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: ')
print(_input_tensor)
_data = [1, 2, 3, 4, 5, 6]
_dtype = torch.float32
_device = torch.device('cpu')
_requires_grad = True
_output_tensor = torch.Tensor.new_tensor(_input_tensor, _data, _dtype, _device, _requires_grad)
print('Output tensor: ')
print(_output_tensor)