'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input_data = torch.randn(2, 3, 5)
print('Input data:')
print(input_data)
output_data = torch.fliplr(input_data)
print('Output data:')
print(output_data)