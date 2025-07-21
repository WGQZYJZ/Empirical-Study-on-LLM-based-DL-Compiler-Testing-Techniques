'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
input_tensor = torch.arange(1, 7).reshape(2, 3)
vec = torch.arange(1, 4)
result = torch.Tensor.mv(input_tensor, vec)
print(result)