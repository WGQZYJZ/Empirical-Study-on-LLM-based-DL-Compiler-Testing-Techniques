'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_equal_\ntorch.Tensor.less_equal_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
other = 0.5
torch.Tensor.less_equal_(input_tensor, other)
print('input_tensor:', input_tensor)
print('other:', other)