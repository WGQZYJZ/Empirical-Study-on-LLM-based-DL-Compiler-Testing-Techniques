'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac_\ntorch.Tensor.igammac_(_input_tensor, other)\n'
import torch
data = torch.rand(10, dtype=torch.float64)
torch.Tensor.igammac_(data, 1.0)
print(data)
torch.Tensor.igammac_(data, 0.5)
print(data)
torch.Tensor.igammac_(data, 0.0)
print(data)
torch.Tensor.igammac_(data, (- 0.5))
print(data)
torch.Tensor.igammac_(data, (- 1.0))
print(data)