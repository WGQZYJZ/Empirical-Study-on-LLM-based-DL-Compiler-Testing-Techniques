'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
output_tensor = input_tensor.msort(dim=0)
print(output_tensor)