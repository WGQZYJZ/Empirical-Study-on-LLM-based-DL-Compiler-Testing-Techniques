'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]], dtype=torch.float)
print('Input data: ')
print(input_data)
max_pool_1d = torch.nn.MaxPool1d(3, stride=2)
output = max_pool_1d(input_data.unsqueeze(0))
print('Output data: ')
print(output)