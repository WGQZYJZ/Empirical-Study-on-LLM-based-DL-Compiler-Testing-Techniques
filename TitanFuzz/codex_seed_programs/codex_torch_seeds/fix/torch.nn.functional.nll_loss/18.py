"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.Tensor([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
target = torch.LongTensor([0, 2, 1])
loss = torch.nn.functional.nll_loss(input, target)
print(loss)