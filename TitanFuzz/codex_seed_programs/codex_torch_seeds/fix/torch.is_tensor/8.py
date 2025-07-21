'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
data = torch.FloatTensor([1, 2])
print(data)
print(torch.is_tensor(data))
print(torch.is_storage(data))
print(torch.is_storage(torch.FloatTensor(2, 3)))
print(torch.is_storage(torch.FloatTensor(2, 3).storage()))