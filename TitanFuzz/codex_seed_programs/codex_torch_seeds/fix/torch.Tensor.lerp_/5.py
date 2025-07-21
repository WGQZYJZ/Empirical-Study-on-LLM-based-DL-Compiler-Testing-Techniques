'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
import torch
input_tensor = torch.randn(10, 10)
end = torch.randn(10, 10)
weight = torch.randn(10, 10)
out = torch.Tensor.lerp_(input_tensor, end, weight)
print(out)