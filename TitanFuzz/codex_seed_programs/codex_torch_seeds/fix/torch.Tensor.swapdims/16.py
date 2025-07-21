'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print(input_tensor)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)
print(output_tensor)
output_tensor = torch.Tensor.swapdims(input_tensor, 1, 2)
print(output_tensor)
output_tensor = torch.Tensor.swapdims(input_tensor, 2, 0)
print(output_tensor)