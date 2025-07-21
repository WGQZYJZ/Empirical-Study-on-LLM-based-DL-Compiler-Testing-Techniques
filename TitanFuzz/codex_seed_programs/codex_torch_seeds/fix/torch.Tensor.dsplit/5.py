'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(0, 24).view(2, 3, 4)
print('input_tensor: ', input_tensor)
print('After call torch.Tensor.dsplit: ', torch.Tensor.dsplit(input_tensor, split_size_or_sections=2))