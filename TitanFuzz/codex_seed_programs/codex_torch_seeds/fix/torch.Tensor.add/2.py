'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_data = torch.rand(2, 3)
output_data = torch.Tensor.add(input_data, input_data)
print(output_data)
output_data = torch.Tensor.add(input_data, input_data, alpha=0.5)
print(output_data)
output_data = torch.Tensor.add(input_data, input_data, alpha=2)
print(output_data)