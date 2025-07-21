"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HingeEmbeddingLoss\ntorch.nn.HingeEmbeddingLoss(margin=1.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.Tensor([[1.0, (- 1.0), (- 1.0), 1.0]]))
target = Variable(torch.LongTensor([0]))
hinge_loss = torch.nn.HingeEmbeddingLoss()
output = hinge_loss(input, target)
print(output)