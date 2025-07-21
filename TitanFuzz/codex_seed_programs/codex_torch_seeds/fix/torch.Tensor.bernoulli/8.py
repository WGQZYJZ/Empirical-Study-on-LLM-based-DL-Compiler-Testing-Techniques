'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
input_tensor = torch.Tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
output_tensor = torch.Tensor([[0, 0, 0], [0, 0, 0]])
import torch
input_tensor = torch.Tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
output_tensor = torch.Tensor([[0, 0, 0], [0, 0, 0]])
torch.Tensor.bernoulli(input_tensor, out=output_tensor)
print(output_tensor)