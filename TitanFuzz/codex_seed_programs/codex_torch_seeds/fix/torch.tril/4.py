'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input)
output = torch.tril(input, diagonal=0)
print(output)
output = torch.tril(input, diagonal=1)
print(output)
output = torch.tril(input, diagonal=(- 1))
print(output)
output = torch.tril(input, diagonal=2)
print(output)
output = torch.tril(input, diagonal=(- 2))
print(output)