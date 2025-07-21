'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.initial_seed\ntorch.random.initial_seed()\n'
import torch
import numpy as np
np.random.seed(1)
input_data = np.random.randn(10, 3)
print('Input data: {}'.format(input_data))
torch.random.initial_seed()
torch.cuda.manual_seed_all(1)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False