'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
matrices = []
for _ in range(10):
    matrices.append(torch.randn(10, 10))
torch.chain_matmul(*matrices)