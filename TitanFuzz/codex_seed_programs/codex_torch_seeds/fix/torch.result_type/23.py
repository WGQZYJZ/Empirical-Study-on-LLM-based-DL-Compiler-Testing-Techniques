'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.result_type\ntorch.result_type(tensor1, tensor2)\n'
import torch
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.double)
torch.result_type(tensor1, tensor2)