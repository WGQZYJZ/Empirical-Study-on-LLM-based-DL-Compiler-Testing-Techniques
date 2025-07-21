'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 100, (4, 4), dtype=torch.int32)
print('Input Tensor:', input_tensor)
torch.Tensor.gcd_(input_tensor, torch.tensor(3))
print('Output Tensor:', input_tensor)