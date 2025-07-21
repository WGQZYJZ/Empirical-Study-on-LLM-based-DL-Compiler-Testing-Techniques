'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
input_tensor = torch.randn(10, 5)
vec = torch.randn(5)
output_tensor = input_tensor.mv(vec)
print(output_tensor)