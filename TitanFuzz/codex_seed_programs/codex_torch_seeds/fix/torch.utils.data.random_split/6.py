'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
import torch.utils.data
input_data = torch.randn(10, 2)
(train_data, test_data) = torch.utils.data.random_split(input_data, [7, 3])
print('train_data: ', train_data)
print('test_data: ', test_data)
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 7])
print('train_data: ', train_data)
print('test_data: ', test_data)
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 7])
print('train_data: ', train_data)