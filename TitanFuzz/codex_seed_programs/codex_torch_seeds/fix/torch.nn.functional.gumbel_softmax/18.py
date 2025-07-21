'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import torch
logits = np.random.rand(5, 2)
logits = torch.from_numpy(logits)
logits = Variable(logits)
output = F.gumbel_softmax(logits)
print(output)