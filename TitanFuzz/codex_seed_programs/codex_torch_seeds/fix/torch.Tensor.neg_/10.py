'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.Tensor.neg_(input_tensor)
print(input_tensor)
input_tensor = torch.randn(2, 3)
print(input_tensor)
input_tensor.neg_()
print(input_tensor)
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = torch.neg(input_tensor)
print(output_tensor)