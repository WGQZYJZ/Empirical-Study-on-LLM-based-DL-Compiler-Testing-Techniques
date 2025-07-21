'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
vec1 = torch.tensor([[10], [20]], dtype=torch.float32)
vec2 = torch.tensor([[100], [200]], dtype=torch.float32)
result = torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)
print(result)