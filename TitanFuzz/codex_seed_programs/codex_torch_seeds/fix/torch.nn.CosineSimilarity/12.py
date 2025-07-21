'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch
input1 = torch.rand(3, 4)
input2 = torch.rand(3, 4)
output = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
print(output(input1, input2))