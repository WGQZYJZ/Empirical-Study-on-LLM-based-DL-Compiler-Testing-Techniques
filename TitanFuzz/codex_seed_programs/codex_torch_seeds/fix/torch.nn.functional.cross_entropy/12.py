"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 5, requires_grad=True)
target_data = torch.empty(1, dtype=torch.long).random_(5)
print(input_data)
print(target_data)
loss = F.cross_entropy(input_data, target_data)
print(loss)
loss.backward()
print(input_data.grad)
weight = torch.tensor([0.1, 1, 0.1, 0.1, 0.1], dtype=torch.float)
loss = F.cross_entropy(input_data, target_data, weight)
print(loss)
loss.backward()