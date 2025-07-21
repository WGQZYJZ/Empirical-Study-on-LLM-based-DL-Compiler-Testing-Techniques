'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
import torch
a = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
b = torch.Tensor.bitwise_left_shift(a, 1)
print(a)
print(b)