'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int\ntorch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = input_data.int()
print(output_data)