'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.rand(3, 3)
print(input)
print(torch.take(input, torch.tensor([0, 1])))
print(torch.take(input, torch.tensor([1, 2])))
print(torch.take(input, torch.tensor([2, 0])))
print(torch.take(input, torch.tensor([0, 1, 2])))