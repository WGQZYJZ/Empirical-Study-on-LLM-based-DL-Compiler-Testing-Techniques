'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
vec1 = torch.tensor([1, 2, 3], dtype=torch.float32)
vec2 = torch.tensor([4, 5, 6], dtype=torch.float32)
output = torch.Tensor.addr_(vec1, vec2, beta=1, alpha=1)
print(output)