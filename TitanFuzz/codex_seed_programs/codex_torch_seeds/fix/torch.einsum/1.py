'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[7, 8], [9, 10], [11, 12]], dtype=torch.float32)
result = torch.einsum('ij,jk->ik', x, y)
print(result)
print(result.shape)
print(result)