'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_tensor: ', input_tensor)
expand_tensor = torch.Tensor.expand(input_tensor, 3)
print('expand_tensor: ', expand_tensor)
expand_tensor = torch.Tensor.expand(input_tensor, 2, 3)
print('expand_tensor: ', expand_tensor)