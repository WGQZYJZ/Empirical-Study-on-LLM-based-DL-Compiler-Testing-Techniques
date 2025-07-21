'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
input_data = torch.arange(1, 6, dtype=torch.float32)
output_data = torch.Tensor.lgamma(input_data)
print('Input: ', input_data)
print('Output:', output_data)