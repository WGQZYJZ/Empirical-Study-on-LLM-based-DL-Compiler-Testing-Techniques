'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.item\ntorch.Tensor.item(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(1, 1, 3, 3)
output = torch.Tensor.item(input_tensor)
print(output)