"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding_bag\ntorch.nn.functional.embedding_bag(input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode='mean', sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None)\n"
import torch
from torch.autograd import Variable
input = Variable(torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]]))
weight = Variable(torch.randn(10, 3))
output = torch.nn.functional.embedding_bag(input, weight, mode='mean')
print(output)