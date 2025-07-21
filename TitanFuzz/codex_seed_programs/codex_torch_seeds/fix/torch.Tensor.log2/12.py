'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 4)
output_tensor = torch.Tensor.log2(input_tensor)
print(output_tensor)