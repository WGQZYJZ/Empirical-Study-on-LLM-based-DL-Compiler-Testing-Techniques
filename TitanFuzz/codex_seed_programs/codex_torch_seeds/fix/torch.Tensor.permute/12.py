'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print(input_tensor)
input_tensor = torch.randn(2, 3, 5)
print(input_tensor)
output_tensor = input_tensor.permute(1, 0, 2)
print(output_tensor)