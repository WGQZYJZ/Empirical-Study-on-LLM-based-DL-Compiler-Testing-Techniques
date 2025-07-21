'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(5, 2, 3)
output_data = input_data.long()
print('Input data:', input_data)
print('Output data:', output_data)