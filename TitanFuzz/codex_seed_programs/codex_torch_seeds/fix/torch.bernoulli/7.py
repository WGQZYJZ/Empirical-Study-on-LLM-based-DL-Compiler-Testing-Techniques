'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input_data = torch.Tensor([0.2, 0.4, 0.6, 0.8])
result = torch.bernoulli(input_data)
print(result)
output_data = torch.Tensor([0.0, 0.0, 0.0, 0.0])
result = torch.bernoulli(input_data, out=output_data)
print(result)
g = torch.Generator()
result = torch.bernoulli(input_data, generator=g)
print(result)
result = torch.bernoulli(input_data, generator=g, out=output_data)
print(result)