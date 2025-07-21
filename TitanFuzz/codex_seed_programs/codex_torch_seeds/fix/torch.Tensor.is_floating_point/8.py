'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor.is_floating_point())
input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
print(input_tensor.is_floating_point())
input_tensor = torch.randint(10, (2, 3), dtype=torch.double)
print(input_tensor.is_floating_point())