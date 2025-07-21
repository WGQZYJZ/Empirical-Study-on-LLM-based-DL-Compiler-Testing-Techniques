'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = input_tensor.lgamma()
print(output_tensor)