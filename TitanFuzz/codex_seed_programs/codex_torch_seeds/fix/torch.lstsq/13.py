'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
input = torch.tensor([[1.0, 1.0, 1.0], [1.0, 2.0, 3.0], [1.0, 3.0, 6.0]], dtype=torch.float64)
A = torch.tensor([[1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 6.0, 8.0], [3.0, 6.0, 9.0, 12.0]], dtype=torch.float64)
output = torch.lstsq(input, A)
print(output)
'\nTask 4: Call the API torch.svd\ntorch.svd(input, *, some=True, compute_uv=True, out=None)\n'
import torch
input = torch.tensor([[1.0, 1.0, 1.0], [1.0, 2.0, 3.0], [1.0, 3.0, 6.0]], dtype=torch.float64)
output = torch.svd(input)
print(output)