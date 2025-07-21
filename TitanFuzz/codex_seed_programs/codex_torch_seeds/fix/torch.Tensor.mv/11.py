'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
import torch
input_tensor = torch.rand(5, 3)
vec = torch.rand(3)
result = torch.Tensor.mv(input_tensor, vec)
print(result)