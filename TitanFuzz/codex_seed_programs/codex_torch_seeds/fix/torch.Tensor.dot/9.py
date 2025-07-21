'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(3, 4)
output_tensor = input_tensor.dot(input_tensor.t())
print(output_tensor)