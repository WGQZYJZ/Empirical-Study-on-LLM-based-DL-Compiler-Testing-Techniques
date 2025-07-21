'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.permute(input_tensor, 1, 2, 0)
print(output_tensor)