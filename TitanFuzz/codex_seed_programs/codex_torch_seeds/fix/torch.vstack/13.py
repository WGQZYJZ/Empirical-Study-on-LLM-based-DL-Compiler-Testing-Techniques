'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
input_data1 = torch.arange(1, 5)
input_data2 = torch.arange(5, 9)
input_data3 = torch.arange(9, 13)
print(torch.vstack((input_data1, input_data2, input_data3)))
print(torch.vstack((input_data1, input_data2, input_data3)).shape)