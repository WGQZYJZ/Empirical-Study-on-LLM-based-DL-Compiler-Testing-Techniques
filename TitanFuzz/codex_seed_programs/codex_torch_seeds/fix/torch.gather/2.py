'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, *, sparse_grad=False, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dim = 1
index = torch.tensor([[1, 1], [0, 2]])
output = torch.gather(input, dim, index)
print(output)