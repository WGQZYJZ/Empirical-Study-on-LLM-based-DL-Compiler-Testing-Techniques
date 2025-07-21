'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
print(x.argmax(dim=0))
print(x.argmax(dim=1))
print(x.argmax(dim=1, keepdim=True))