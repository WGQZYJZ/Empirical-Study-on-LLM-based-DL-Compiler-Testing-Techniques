'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch.nn as nn
input_tensor_1 = torch.rand(2, 3)
input_tensor_2 = torch.rand(2, 3)
cos_sim = nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos_sim(input_tensor_1, input_tensor_2)
print(output)