'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input)
topk_output = torch.topk(input, 2)
print(topk_output)
print(topk_output[0])
print(topk_output[1])