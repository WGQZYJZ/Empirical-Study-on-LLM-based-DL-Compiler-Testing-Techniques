'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
from torch.utils.data import Subset
dataset = torch.randn(10, 3)
indices = [1, 3, 5]
new_dataset = Subset(dataset, indices)
print('new_dataset: ', new_dataset)
print('new_dataset.indices: ', new_dataset.indices)
print('new_dataset.dataset: ', new_dataset.dataset)