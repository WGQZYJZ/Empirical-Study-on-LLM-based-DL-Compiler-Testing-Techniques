'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
matrix_a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
matrix_b = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
matrix_c = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
result = torch.chain_matmul(matrix_a, matrix_b, matrix_c)
print(result)