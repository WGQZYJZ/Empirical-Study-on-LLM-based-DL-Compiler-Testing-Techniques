'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.item\ntorch.Tensor.item(_input_tensor)\n'
import torch
input_tensor = torch.randn((1, 2))
output = input_tensor.item()
print(output)