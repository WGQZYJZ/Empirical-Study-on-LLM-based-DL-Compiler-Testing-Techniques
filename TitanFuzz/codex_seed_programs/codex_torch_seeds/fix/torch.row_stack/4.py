'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
input_tensor_1 = torch.rand(2, 3)
input_tensor_2 = torch.rand(2, 3)
input_tensor_3 = torch.rand(2, 3)
output_tensor = torch.row_stack((input_tensor_1, input_tensor_2, input_tensor_3))
print(output_tensor)