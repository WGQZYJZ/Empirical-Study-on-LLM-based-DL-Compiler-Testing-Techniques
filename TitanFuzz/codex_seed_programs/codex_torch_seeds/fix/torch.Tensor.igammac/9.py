'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac\ntorch.Tensor.igammac(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.igammac(input_tensor, 2)
print(output_tensor)