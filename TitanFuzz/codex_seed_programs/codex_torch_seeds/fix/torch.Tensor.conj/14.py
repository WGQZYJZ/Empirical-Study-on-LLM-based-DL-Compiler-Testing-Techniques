'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj\ntorch.Tensor.conj(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
output_tensor = input_tensor.conj()
print(output_tensor)