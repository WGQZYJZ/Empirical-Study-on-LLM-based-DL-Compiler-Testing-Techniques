'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.DoubleStorage\ntorch.DoubleStorage(*args, **kwargs)\n'
import torch
import torch
input_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
double_storage = torch.DoubleStorage(input_data)
print('double_storage = ', double_storage)
print('The type of double_storage is ', type(double_storage))
print('The size of double_storage is ', double_storage.size())
print('The value of double_storage is ', double_storage.tolist())
print('The element of double_storage is ', double_storage[0])