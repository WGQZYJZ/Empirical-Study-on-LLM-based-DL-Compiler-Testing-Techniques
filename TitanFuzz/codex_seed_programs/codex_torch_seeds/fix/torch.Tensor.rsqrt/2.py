'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt\ntorch.Tensor.rsqrt(_input_tensor)\n'
import torch
input_tensor = torch.rand((1, 2, 3, 4), dtype=torch.float32)
import torch
input_tensor = torch.rand((1, 2, 3, 4), dtype=torch.float32)
output_tensor = input_tensor.rsqrt()
print(output_tensor)