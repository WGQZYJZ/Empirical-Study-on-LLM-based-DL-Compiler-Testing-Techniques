'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
input_data = torch.rand(5, 3)
print(input_data)
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 2])
print(train_data)
print(test_data)