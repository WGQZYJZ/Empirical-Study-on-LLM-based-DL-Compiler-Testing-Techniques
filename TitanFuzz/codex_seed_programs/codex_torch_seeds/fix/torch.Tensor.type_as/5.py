'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
data_input = torch.randn(2, 3)
print(data_input)
data_output = data_input.type_as(torch.FloatTensor())
print(data_output)
data_output = data_input.type_as(torch.DoubleTensor())
print(data_output)