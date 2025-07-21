'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh_\ntorch.Tensor.cosh_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 2)
output_tensor = input_tensor.cosh_()
print(output_tensor)