'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
input_data = torch.randn(100, 10)
split_data = torch.utils.data.random_split(input_data, [20, 80])
print(split_data)