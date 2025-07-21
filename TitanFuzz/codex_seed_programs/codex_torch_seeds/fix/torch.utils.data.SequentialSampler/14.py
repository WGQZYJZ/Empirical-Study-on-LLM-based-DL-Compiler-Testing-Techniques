'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
data_source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
torch.utils.data.SequentialSampler(data_source)