'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input data:')
print(input_data)
flipped_data = torch.fliplr(input_data)
print('Flipped data:')
print(flipped_data)