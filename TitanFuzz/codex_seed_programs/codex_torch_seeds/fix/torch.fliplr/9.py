'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input = torch.randn(1, 10, 10)
output = torch.fliplr(input)
print(input)
print(output)