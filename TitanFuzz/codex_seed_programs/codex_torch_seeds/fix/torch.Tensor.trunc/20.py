'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, dtype=torch.float32)
print('Input tensor is:', input_tensor)
trunc_tensor = input_tensor.trunc()
print('Trunc tensor is:', trunc_tensor)