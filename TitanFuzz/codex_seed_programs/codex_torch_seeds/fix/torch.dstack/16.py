'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
print(torch.__version__)
input_data = torch.rand(3, 4, 5)
print(input_data.shape)
output_data = torch.dstack((input_data, input_data))
print(output_data.shape)