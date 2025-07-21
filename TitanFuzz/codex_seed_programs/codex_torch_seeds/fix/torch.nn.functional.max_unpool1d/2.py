'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool1d\ntorch.nn.functional.max_unpool1d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
import torch.nn.functional as F
input = torch.tensor([[[1, 2, 3, 4]]], dtype=torch.float)
indices = torch.tensor([[[0, 1, 1, 0]]], dtype=torch.long)
F.max_unpool1d(input, indices, kernel_size=2, stride=2, padding=0)