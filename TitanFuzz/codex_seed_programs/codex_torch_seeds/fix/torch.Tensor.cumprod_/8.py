'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = input_data.cumprod_(1)
print(output_data)
output_data = input_data.cumprod_(0)
print(output_data)