'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch.nn as nn
input_data = torch.rand(3, 5)
cos_sim = nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos_sim(input_data, input_data)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input_data = torch.rand(5, 3)
target = torch.empty(5, dtype=torch.long).random_(3)
ce_loss = nn.CrossEntropyLoss()
output = ce_loss(input_data, target)
print(output)