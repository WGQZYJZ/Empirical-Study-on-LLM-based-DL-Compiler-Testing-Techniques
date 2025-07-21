"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
input = torch.autograd.Variable(torch.randn(3, 5), requires_grad=True)
target = torch.autograd.Variable(torch.LongTensor(3).random_(5))
loss = torch.nn.NLLLoss()
output = loss.forward(input, target)
print('output: ', output)
print('grad: ', input.grad)