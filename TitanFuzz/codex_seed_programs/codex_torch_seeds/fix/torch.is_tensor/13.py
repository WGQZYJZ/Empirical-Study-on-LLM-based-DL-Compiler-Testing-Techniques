'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
c = [1, 2]
d = (1, 2)
e = 1
f = 'hello'
g = {'a': 1, 'b': 2}
print('a: ', torch.is_tensor(a))
print('b: ', torch.is_tensor(b))
print('c: ', torch.is_tensor(c))
print('d: ', torch.is_tensor(d))
print('e: ', torch.is_tensor(e))
print('f: ', torch.is_tensor(f))
print('g: ', torch.is_tensor(g))