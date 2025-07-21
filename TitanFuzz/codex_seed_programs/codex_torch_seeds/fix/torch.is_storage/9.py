'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
input_data = torch.rand(3, 3)
print('Input data:\n{}'.format(input_data))
output = torch.is_storage(input_data)
print('Output:\n{}'.format(output))