'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix\ntorch.Tensor.fix(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
fixed_tensor = torch.Tensor.fix(input_tensor)
print(fixed_tensor)