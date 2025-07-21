'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
tensor_1 = torch.tensor([[1, 2], [3, 4]])
tensor_2 = torch.tensor([[5, 6], [7, 8]])
tensor_3 = torch.tensor([[9, 10], [11, 12]])
torch.block_diag(tensor_1, tensor_2, tensor_3)