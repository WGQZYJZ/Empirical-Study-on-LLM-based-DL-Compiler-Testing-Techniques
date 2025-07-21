'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other_data = torch.Tensor([[1, 1, 1], [1, 1, 1]])
print(torch.less(input_data, other_data))