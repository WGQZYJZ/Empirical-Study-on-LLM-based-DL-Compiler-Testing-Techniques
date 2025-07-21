'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal_\ntorch.Tensor.reciprocal_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
reciprocal_tensor = torch.reciprocal(input_tensor)
print(reciprocal_tensor)
reciprocal_tensor = torch.reciprocal_(input_tensor)
print(reciprocal_tensor)
reciprocal_tensor = input_tensor.reciprocal_()
print(reciprocal_tensor)
reciprocal_tensor = input_tensor.reciprocal()
print(reciprocal_tensor)