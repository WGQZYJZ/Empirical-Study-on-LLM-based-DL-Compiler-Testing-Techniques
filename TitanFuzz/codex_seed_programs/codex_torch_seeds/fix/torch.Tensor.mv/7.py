'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
vec = torch.randn(4)
output_tensor = torch.Tensor.mv(input_tensor, vec)
print(output_tensor)