'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
from torch.utils.data import Subset
import numpy as np
data = np.arange(1, 11)
indices = [1, 3, 5, 7, 9]
subset = Subset(data, indices)
print(subset)