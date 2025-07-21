'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
output_tensor = input_tensor.trunc()
print(output_tensor)
output_tensor = torch.trunc(input_tensor)
print(output_tensor)