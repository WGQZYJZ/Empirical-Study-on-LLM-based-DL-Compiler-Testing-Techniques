'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
input_tensor = torch.arange(1, 7)
print(input_tensor)
output_tensor = input_tensor.view(2, 3)
print(output_tensor)