'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trace\ntorch.Tensor.trace(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
print(input_tensor.trace())
input_tensor = torch.rand(4, 4)
print(input_tensor)
print(input_tensor.trace())