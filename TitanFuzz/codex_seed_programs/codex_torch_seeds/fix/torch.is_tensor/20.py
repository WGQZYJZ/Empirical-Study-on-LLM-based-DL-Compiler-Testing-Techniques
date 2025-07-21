'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
data1 = [1, 2, 3]
data2 = [[1, 2, 3], [4, 5, 6]]
data3 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
print(torch.is_tensor(data1))
print(torch.is_tensor(data2))
print(torch.is_tensor(data3))