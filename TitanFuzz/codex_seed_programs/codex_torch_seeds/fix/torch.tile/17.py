'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.randn(2, 3)
print('Input: ', input)
print('Tile: ', torch.tile(input, (1, 2)))
print('Tile: ', torch.tile(input, (2, 1)))
print('Tile: ', torch.tile(input, (2, 2)))