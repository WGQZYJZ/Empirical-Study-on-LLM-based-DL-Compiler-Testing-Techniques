'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.DoubleStorage\ntorch.DoubleStorage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5]
print(input_data)
input_storage = torch.DoubleStorage(input_data)
print(input_storage)
print(input_storage.size())
print(input_storage[0])
print(input_storage[1])
print(input_storage[2])
print(input_storage[3])
print(input_storage[4])