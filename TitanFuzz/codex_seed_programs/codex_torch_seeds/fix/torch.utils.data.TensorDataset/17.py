'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
import torch
x = np.random.randn(1000, 3)
y = np.random.randint(0, 2, size=(1000, 1))
dataset = torch.utils.data.TensorDataset(torch.tensor(x, dtype=torch.float32), torch.tensor(y))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
import torch
x = np.random.randn(1000, 3)
y = np.random.randint(0, 2, size=(1000, 1))