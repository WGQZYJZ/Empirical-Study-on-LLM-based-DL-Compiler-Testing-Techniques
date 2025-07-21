'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(3, 3)
end = torch.ones(3, 3)
weight = 0.5
torch.Tensor.lerp_(input_tensor, end, weight)
print(input_tensor)