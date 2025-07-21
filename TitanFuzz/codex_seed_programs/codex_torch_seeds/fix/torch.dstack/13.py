'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
input_tensor_1 = torch.randn(2, 3, 4)
input_tensor_2 = torch.randn(2, 3, 4)
print(input_tensor_1)
print(input_tensor_2)
output_tensor = torch.dstack((input_tensor_1, input_tensor_2))
print(output_tensor)