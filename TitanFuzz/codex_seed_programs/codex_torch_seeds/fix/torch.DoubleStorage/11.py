'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.DoubleStorage\ntorch.DoubleStorage(*args, **kwargs)\n'
import torch
data = [1.0, 2.0, 3.0]
data_storage = torch.DoubleStorage(data)
print(data_storage)