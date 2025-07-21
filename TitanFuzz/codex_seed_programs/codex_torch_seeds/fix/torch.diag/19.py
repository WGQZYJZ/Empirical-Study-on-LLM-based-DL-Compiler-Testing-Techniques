'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: \n', input)
diagonal = torch.diag(input)
print('Diagonal: \n', diagonal)
diagonal_1 = torch.diag(input, diagonal=1)
print('Diagonal 1: \n', diagonal_1)
diagonal_2 = torch.diag(input, diagonal=2)
print('Diagonal 2: \n', diagonal_2)
diagonal_3 = torch.diag(input, diagonal=3)
print('Diagonal 3: \n', diagonal_3)