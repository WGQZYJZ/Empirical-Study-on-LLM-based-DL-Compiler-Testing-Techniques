'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.cummax(input_tensor, dim=0)
print(output_tensor)