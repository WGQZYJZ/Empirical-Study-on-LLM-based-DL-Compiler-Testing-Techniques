'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
end = torch.tensor([[10, 20, 30], [40, 50, 60]])
weight = 0.5
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)
print(output_tensor)