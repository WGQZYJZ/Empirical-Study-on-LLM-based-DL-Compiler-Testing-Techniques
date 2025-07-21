'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_available\ntorch.distributed.is_available()\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = torch.tensor([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
print(torch.distributed.is_available())