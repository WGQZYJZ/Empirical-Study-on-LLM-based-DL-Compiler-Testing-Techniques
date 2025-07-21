'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter\ntorch.Tensor.nextafter(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(4, 4)
print(torch.Tensor.nextafter(input_tensor, torch.rand(4, 4)))