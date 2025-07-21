"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding_bag\ntorch.nn.functional.embedding_bag(input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode='mean', sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None)\n"
import torch
import torch.nn.functional as F
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.LongTensor([[1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0]])
weight = torch.FloatTensor([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print('Task 3: Call the API torch.nn.functional.embedding_bag')
print(F.embedding_bag(input, weight, mode='mean'))