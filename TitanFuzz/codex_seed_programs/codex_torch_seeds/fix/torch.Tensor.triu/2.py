'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = input_tensor.triu(diagonal=0)
print(input_tensor)
print(output_tensor)