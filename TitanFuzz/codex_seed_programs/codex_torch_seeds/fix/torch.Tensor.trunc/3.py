'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
truncated_tensor = input_tensor.trunc()
print('The truncated tensor is: ', truncated_tensor)
print('The original tensor is: ', input_tensor)