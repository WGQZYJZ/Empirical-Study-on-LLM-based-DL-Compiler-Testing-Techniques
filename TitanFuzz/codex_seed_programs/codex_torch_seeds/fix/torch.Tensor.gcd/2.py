'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[12, 15], [18, 30]], dtype=torch.int32)
other = torch.tensor([[6, 5], [9, 10]], dtype=torch.int32)
print(torch.Tensor.gcd(input_tensor, other))