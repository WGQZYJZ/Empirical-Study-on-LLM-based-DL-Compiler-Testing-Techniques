'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = input_tensor.polygamma(3)
print(output_tensor)