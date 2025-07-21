'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
input_tensor = torch.randn((1, 3, 3))
print(input_tensor)
output_tensor = torch.Tensor.positive(input_tensor)
print(output_tensor)