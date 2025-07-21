'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
data = [[1, 2, 3], [4, 5, 6]]
torch.get_default_dtype()
torch.tensor(data)
torch.as_tensor(data)
import numpy as np
np_data = np.array(data)
torch.from_numpy(np_data)
torch.eye(2)
torch.zeros(2, 3)
torch.ones(2, 3)
torch.rand(2, 3)