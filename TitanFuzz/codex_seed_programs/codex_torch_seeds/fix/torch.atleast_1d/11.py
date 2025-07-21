'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
input_data = torch.rand(1, 2, 3, 4)
output_data = torch.atleast_1d(input_data)
print(output_data.size())
output_data = torch.atleast_2d(input_data)
print(output_data.size())
output_data = torch.atleast_3d(input_data)
print(output_data.size())