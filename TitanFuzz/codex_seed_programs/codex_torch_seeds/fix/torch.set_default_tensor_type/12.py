'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
x = torch.tensor([[2, 3, 4], [5, 6, 7]])
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.set_default_tensor_type(torch.FloatTensor)
print((x + y))
print(x.dtype)