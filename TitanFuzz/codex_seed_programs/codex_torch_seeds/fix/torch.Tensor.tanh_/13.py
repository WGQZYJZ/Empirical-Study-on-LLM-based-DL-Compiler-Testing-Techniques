'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tanh_\ntorch.Tensor.tanh_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input data: ', _input_tensor)
_tanh_output = torch.Tensor.tanh_(_input_tensor)
print('Tanh output: ', _tanh_output)