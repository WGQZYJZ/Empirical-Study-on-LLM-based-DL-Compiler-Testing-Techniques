'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(4, 3)
print('input_tensor = ', input_tensor)
expanded_tensor = input_tensor.expand(4, 5)
print('expanded_tensor = ', expanded_tensor)