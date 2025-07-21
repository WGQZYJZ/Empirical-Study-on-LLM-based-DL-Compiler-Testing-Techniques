'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
input_data = torch.Tensor([1, 2, 3, 4, 5])
torch._assert(torch.all((input_data > 0)), 'Input data must be positive')