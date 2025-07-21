'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.randint(low=0, high=10, size=(2, 3, 4))
print('Input: ', input)
rot90_input = torch.rot90(input, k=1, dims=(1, 2))
print('Rotate by 90 degree: ', rot90_input)
rot180_input = torch.rot90(input, k=2, dims=(1, 2))
print('Rotate by 180 degree: ', rot180_input)
rot270_input = torch.rot90(input, k=3, dims=(1, 2))
print('Rotate by 270 degree: ', rot270_input)