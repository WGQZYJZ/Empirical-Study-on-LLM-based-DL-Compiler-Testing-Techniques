'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input = torch.randn(3, 4, 5)
output = torch.movedim(input, 0, 2)
print(input)
print(output)