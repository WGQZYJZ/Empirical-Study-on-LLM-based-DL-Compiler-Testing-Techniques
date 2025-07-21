'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
output_tensor = torch.Tensor.neg_(input_tensor)
print(input_tensor)