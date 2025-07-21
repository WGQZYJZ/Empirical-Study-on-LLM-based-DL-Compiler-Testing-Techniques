'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
matrix = torch.rand(2, 3)
vector = torch.rand(3)
print(matrix)
print(vector)
print(torch.mv(matrix, vector))