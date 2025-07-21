'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.rand(2, 3)
print(torch.Tensor.heaviside(input_tensor, 0.5))