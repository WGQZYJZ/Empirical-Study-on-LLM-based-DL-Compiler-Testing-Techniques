'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
import torch
input_data_1 = torch.rand(2, 3)
input_data_2 = torch.rand(2, 3)
torch.column_stack((input_data_1, input_data_2))
print(torch.column_stack((input_data_1, input_data_2)))
print(torch.column_stack((input_data_1, input_data_2)).shape)
print(torch.column_stack((input_data_1, input_data_2)).type())
print(torch.column_stack((input_data_1, input_data_2)).dim())