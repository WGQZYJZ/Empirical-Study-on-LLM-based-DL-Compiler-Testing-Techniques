'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
print(input_tensor)
output_tensor = input_tensor.swapdims(1, 2)
print(output_tensor)