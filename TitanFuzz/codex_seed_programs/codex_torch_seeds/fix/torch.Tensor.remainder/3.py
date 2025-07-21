'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder\ntorch.Tensor.remainder(_input_tensor, divisor)\n'
import torch
input_tensor = torch.rand(2, 3)
divisor = torch.tensor([1, 2, 3])
print(input_tensor)
print(input_tensor.remainder(divisor))