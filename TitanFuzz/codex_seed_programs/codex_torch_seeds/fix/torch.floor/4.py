'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1.1, 2.3, 4.5], [6.7, 8.9, 10.1]], dtype=torch.float32)
output_data = torch.floor(input_data)
print('Input:')
print(input_data)
print('Output:')
print(output_data)