'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(4, 4)
end = torch.ones(4, 4)
weight = 0.5
output_tensor = input_tensor.lerp(end, weight)
print(output_tensor)