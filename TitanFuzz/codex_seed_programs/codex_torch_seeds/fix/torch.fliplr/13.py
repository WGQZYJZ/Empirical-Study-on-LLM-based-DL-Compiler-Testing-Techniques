'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input = torch.randn(2, 3, 5)
output = torch.fliplr(input)
print(input)
print(output)