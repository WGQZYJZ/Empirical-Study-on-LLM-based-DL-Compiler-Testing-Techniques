'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
a = torch.tensor([1.0, 2.0, 3.0, 4.0])
b = torch.tensor([1.0, 2.0, 3.001, 3.999])
c = torch.tensor([1.0, 2.0, 3.0, 4.0])
print(torch.isclose(a, b, rtol=0.01, atol=0.001))
print(torch.isclose(a, c))