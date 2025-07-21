'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output = input_tensor.is_conj()
print(output)