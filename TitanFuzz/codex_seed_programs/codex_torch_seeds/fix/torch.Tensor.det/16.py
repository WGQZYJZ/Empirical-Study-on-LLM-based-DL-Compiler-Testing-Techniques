'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 3)
output_tensor = torch.Tensor.det(input_tensor)
print(output_tensor)