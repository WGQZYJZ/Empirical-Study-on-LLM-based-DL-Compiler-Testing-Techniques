'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
vector = torch.tensor([5, 6], dtype=torch.float32)
torch.Tensor.addmv_(matrix, matrix, vector)
print(matrix)