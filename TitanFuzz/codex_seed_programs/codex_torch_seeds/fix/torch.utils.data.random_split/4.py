'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
input_data = torch.arange(1, 11)
print('Input Data:', input_data)
split_data = torch.utils.data.random_split(input_data, [3, 7])
print('Split Data:', split_data)