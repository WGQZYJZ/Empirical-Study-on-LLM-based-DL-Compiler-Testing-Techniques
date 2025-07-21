'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(5, 3)
output_tensor = torch.Tensor.equal(input_tensor, input_tensor)
print(input_tensor)
print(output_tensor)