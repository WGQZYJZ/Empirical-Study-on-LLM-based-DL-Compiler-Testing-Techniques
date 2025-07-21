'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pinverse\ntorch.Tensor.pinverse(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
pseudo_inverse = input_tensor.pinverse()
print(pseudo_inverse)