'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0\ntorch.Tensor.i0(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 4)
output_tensor = torch.Tensor.i0(input_tensor)
print(output_tensor)