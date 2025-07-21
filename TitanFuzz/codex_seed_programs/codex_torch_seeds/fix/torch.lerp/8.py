'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[10, 20], [30, 40]], dtype=torch.float32)
out = torch.lerp(x, y, 0.5)
print(out)