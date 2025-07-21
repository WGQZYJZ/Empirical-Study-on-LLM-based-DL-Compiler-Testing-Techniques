'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
is_complex = input_tensor.is_complex()
print('is_complex: ', is_complex)