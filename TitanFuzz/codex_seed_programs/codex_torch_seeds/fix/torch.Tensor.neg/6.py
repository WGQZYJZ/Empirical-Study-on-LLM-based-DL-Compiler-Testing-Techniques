'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.neg(input_tensor)
print(output_tensor)