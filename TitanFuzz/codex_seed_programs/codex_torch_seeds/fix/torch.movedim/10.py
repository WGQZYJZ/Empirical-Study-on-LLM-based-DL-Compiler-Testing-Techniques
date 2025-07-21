'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input_data = torch.randn(3, 4, 5)
print('Input data: ', input_data)
print('\nMove the dimension at position 1 to position 2: ')
print(torch.movedim(input_data, 1, 2))
print('\nMove the dimension at position 1 to position 0: ')
print(torch.movedim(input_data, 1, 0))
print('\nMove the dimension at position 1 to position -1: ')
print(torch.movedim(input_data, 1, (- 1)))
print('\nMove the dimension at position 2 to position -1: ')
print(torch.movedim(input_data, 2, (- 1)))