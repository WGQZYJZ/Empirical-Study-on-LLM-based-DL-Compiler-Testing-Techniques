'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, other)
print(input_tensor)