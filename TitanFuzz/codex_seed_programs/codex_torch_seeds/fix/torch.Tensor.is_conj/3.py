'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float32)
print('Input tensor: ', input_tensor)
print('Is conjugate: ', input_tensor.is_conj())