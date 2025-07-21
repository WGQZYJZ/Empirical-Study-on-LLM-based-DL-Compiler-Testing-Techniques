'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(5, 3)
end = torch.rand(5, 3)
weight = torch.rand(5, 3)
print(torch.Tensor.lerp(input_tensor, end, weight))