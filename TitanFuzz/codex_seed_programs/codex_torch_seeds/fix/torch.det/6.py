'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
input = torch.tensor([[2, 3], [4, 5]], dtype=torch.float32)
print('Input: ', input)
print('Determinant of input: ', torch.det(input))