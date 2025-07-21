'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
print(torch.movedim(input, 0, 1))