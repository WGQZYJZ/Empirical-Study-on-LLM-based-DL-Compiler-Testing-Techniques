'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(torch.Tensor.det(input_tensor))