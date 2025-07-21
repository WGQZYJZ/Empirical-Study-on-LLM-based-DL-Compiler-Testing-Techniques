'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isnan\ntorch.Tensor.isnan(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[0, 1, float('nan'), 3], [4, float('nan'), 6, 7]])
_output_tensor = torch.Tensor.isnan(_input_tensor)
print('input tensor:')
print(_input_tensor)
print('output tensor:')
print(_output_tensor)