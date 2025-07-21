'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
matrices = []
for i in range(5):
    matrices.append(torch.rand(5, 5))
result = torch.chain_matmul(*matrices)
print(result)