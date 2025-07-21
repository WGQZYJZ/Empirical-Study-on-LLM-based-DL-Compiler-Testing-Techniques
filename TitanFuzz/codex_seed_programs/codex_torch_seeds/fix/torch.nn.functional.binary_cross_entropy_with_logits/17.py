"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.binary_cross_entropy_with_logits\ntorch.nn.functional.binary_cross_entropy_with_logits(input, target, weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import numpy as np
input = torch.tensor(np.random.rand(10, 1), dtype=torch.float32)
target = torch.tensor(np.random.randint(2, size=(10, 1)), dtype=torch.float32)
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)
print('loss =', loss)