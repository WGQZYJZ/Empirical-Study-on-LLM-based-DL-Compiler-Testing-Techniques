'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
import numpy as np
x = np.array([[1, 2], [3, 4]])
y = torch.from_numpy(x)
print(y)
print(y.type())
torch.set_default_tensor_type(torch.FloatTensor)
z = torch.from_numpy(x)
print(z)
print(z.type())