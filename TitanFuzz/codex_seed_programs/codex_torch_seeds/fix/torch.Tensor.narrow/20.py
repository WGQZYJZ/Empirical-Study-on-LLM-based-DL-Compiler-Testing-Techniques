'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
a = torch.arange(0, 24).view(2, 3, 4)
print(a)
b = a.narrow(1, 1, 2)
print(b)