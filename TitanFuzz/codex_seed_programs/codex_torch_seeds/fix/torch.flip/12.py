'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: ')
print(input)
flipped_input = torch.flip(input, [0])
print('Flipped data: ')
print(flipped_input)