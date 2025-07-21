'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
input_data = [torch.rand(2, 3), torch.rand(4, 3), torch.rand(4, 3)]
output = torch.block_diag(*input_data)
print(output)