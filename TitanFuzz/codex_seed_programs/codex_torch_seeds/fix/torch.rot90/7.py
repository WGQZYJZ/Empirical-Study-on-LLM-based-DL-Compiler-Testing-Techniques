'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.randn(2, 3, 4, 5)
print('Input:', input)
print('Rotate 90 degree:', torch.rot90(input, 1, (2, 3)))
print('Rotate 180 degree:', torch.rot90(input, 2, (2, 3)))
print('Rotate 270 degree:', torch.rot90(input, 3, (2, 3)))
print('Rotate 90 degree:', torch.rot90(input, 1, (1, 2)))
print('Rotate 180 degree:', torch.rot90(input, 2, (1, 2)))
print('Rotate 270 degree:', torch.rot90(input, 3, (1, 2)))