"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
label_data = torch.tensor([1, 0])
loss_func = nn.CrossEntropyLoss()
loss_value = loss_func(input_data, label_data)
print(loss_value)
loss_value_2 = nn.functional.cross_entropy(input_data, label_data)
print(loss_value_2)