import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[1, 1], [4, 4]], dtype=torch.float32)
z = torch.greater_equal(x, y)