'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.Tensor.neg_(input_data)
print(output_data)