'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ShortStorage\ntorch.ShortStorage(*args, **kwargs)\n'
import torch
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data)
print(type(data))
data_tensor = torch.FloatTensor(data)
print(data_tensor)
print(type(data_tensor))
torch_storage = torch.ShortStorage(data)
print(torch_storage)
print(type(torch_storage))