'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
import torch
input_data = torch.arange(0, 10)
print('Input data: ', input_data)
split_data = torch.utils.data.random_split(input_data, [7, 3])
print('Split data: ', split_data)