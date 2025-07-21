'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
input_data1 = torch.randn(1, 2, 3, 4)
input_data2 = torch.randn(1, 2, 3, 4)
output = torch.cat((input_data1, input_data2), dim=0)
print(output.shape)
print('End of the program')