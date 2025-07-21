"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_embedding_loss\ntorch.nn.functional.cosine_embedding_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input1 = Variable(torch.randn(100, 128))
input2 = Variable(torch.randn(100, 128))
target = Variable(torch.Tensor(100).random_(2))
loss = torch.nn.functional.cosine_embedding_loss(input1, input2, target)
print(loss)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=True, ignore_index=-100, reduce=True, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch