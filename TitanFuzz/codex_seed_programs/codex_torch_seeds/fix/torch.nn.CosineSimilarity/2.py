'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(input1, input2)
print(output)