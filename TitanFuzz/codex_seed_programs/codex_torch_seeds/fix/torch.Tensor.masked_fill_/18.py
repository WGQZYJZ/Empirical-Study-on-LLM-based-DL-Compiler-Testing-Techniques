'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 1, 0]])
value = 0.5
input_tensor.masked_fill_(mask, value)
print(input_tensor)