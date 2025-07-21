'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input = torch.randn(3, 3)
print(input)
output = torch.fliplr(input)
print(output)