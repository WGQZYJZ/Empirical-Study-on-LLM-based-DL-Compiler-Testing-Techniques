'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, dtype=torch.float)
print(input_tensor)
output_tensor = input_tensor.frac()
print(output_tensor)