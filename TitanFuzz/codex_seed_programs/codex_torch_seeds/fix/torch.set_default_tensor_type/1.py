'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
data = data.astype(np.float32)
x = torch.from_numpy(data)
print('x = ', x)
torch.set_default_tensor_type(torch.FloatTensor)
print(torch.get_default_dtype())