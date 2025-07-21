'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
input_tensor = torch.empty(100, 100)
'\nTask 4: Generate output data\n'
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5, generator=None)
print(output_tensor)