'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 10)
output_tensor = torch.Tensor.signbit(input_tensor)
print(output_tensor)