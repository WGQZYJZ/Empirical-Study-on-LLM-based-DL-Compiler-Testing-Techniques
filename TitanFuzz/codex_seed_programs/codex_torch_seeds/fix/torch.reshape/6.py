'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
x = torch.randn(2, 3, 4)
print('Input tensor x:')
print(x)
y = torch.reshape(x, (3, 8))
print('Output tensor y:')
print(y)
z = torch.reshape(x, (1, (- 1)))
print('Output tensor z:')
print(z)
w = torch.reshape(x, ((- 1), 1))
print('Output tensor w:')
print(w)