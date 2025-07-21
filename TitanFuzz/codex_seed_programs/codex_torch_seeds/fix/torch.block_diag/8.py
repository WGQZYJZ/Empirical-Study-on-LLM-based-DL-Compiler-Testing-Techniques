'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
tensor3 = torch.rand(2, 3)
result = torch.block_diag(tensor1, tensor2, tensor3)
print('The result is:\n', result)