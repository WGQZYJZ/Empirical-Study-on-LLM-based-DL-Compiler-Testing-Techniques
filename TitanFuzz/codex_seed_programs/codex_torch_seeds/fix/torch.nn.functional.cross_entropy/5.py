"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
input_data = torch.tensor([[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]])
target_data = torch.tensor([1, 0])
loss = torch.nn.functional.cross_entropy(input_data, target_data)
print(loss)