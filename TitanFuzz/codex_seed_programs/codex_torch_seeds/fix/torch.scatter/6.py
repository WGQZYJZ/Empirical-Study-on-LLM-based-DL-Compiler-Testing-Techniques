'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter\ntorch.scatter(input, dim, index, src)\n'
import torch
input = torch.randn(2, 3)
print(input)
index = torch.tensor([[0, 1, 0], [1, 0, 0]])
print(index)
output = torch.zeros(2, 3)
torch.scatter(output, 0, index, input)
print(output)
output = torch.zeros(2, 3)
torch.scatter(output, 1, index, input)
print(output)