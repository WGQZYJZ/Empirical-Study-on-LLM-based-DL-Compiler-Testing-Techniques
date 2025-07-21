'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.FloatStorage\ntorch.FloatStorage(*args, **kwargs)\n'
import torch
if True:
    data = [1, 2, 3, 4, 5]
    data_storage = torch.FloatStorage(data)
    print(data_storage)