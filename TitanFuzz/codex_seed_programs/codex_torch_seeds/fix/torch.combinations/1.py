'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.combinations\ntorch.combinations(input, r=2, with_replacement=False)\n'
import torch
input = torch.arange(1, 5)
print(torch.combinations(input, 2))
print(torch.combinations(input, 3))
print(torch.combinations(input, 4))
print(torch.combinations(input, 5))