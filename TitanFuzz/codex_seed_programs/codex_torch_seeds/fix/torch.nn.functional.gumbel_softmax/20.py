'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import numpy as np
from torch.nn.functional import gumbel_softmax
logits = torch.rand(10, 10)
tau = 1
hard = False
eps = 1e-10
dim = (- 1)
gumbel_softmax(logits, tau, hard, eps, dim)