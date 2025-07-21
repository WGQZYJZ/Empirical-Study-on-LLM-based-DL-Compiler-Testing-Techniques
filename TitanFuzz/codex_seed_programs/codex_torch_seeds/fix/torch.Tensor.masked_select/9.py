'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
input_tensor = torch.randn(4, 5)
mask = torch.ByteTensor([[0, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]])
print(input_tensor.masked_select(mask))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
input_tensor = torch.randn(4, 5)
mask = torch.ByteTensor([[0, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]])
print(input_tensor.masked_select(mask))