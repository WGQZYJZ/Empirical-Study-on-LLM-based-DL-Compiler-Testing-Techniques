'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
input_tensor = torch.arange(1, 17).view(4, 4)
print(input_tensor)
input_tensor = torch.arange(1, 17).view(4, 4)
output_tensor = input_tensor.permute(1, 0)
print(output_tensor)