'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma_\ntorch.Tensor.digamma_(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 4, 5)
digamma_result = torch.Tensor.digamma_(input_tensor)
print(digamma_result)