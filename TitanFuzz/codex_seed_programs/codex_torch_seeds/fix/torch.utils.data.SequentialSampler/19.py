'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
from torch.utils.data import TensorDataset, SequentialSampler
input_ids = torch.tensor([[31, 51, 99], [15, 5, 0], [33, 11, 51]])
attention_masks = torch.tensor([[1, 1, 1], [1, 1, 0], [1, 1, 1]])
labels = torch.tensor([1, 0, 1])
dataset = TensorDataset(input_ids, attention_masks, labels)
sampler = SequentialSampler(dataset)
for batch in sampler:
    print(batch)
'\n[0, 1, 2]\n'