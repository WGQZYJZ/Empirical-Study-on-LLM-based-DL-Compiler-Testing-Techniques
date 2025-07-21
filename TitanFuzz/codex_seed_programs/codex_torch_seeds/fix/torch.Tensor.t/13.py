'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.randn((3, 5), dtype=torch.float32)
print(input_tensor)
output_tensor = input_tensor.t()
print(output_tensor)