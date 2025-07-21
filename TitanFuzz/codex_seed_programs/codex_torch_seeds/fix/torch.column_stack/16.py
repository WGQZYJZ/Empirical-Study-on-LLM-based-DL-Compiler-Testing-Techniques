'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
input_data_1 = torch.rand(3, 1)
input_data_2 = torch.rand(3, 1)
output_data = torch.column_stack((input_data_1, input_data_2))
print('output_data:\n', output_data)