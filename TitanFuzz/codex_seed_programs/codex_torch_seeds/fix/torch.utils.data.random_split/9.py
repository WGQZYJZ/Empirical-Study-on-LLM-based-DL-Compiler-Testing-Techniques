'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
input_data = torch.arange(1, 101).view(10, 10)
print('Input data: \n', input_data)
print('\nTask 2: Generate input data')
print('\nTask 3: Call the API torch.utils.data.random_split')
(train_dataset, test_dataset) = torch.utils.data.random_split(input_data, [8, 2])
print('Training dataset: \n', train_dataset)
print('Testing dataset: \n', test_dataset)