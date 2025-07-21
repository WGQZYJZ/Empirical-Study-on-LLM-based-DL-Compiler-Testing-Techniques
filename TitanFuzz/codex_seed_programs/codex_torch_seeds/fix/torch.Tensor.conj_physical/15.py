'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4, 5)
output_tensor = torch.Tensor.conj_physical(input_tensor)
print(input_tensor)
print(output_tensor)