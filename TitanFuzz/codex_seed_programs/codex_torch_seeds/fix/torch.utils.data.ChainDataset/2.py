'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ChainDataset\ntorch.utils.data.ChainDataset(datasets)\n'
import torch
import torch.utils.data
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[1, 2], [3, 4], [5, 6]])
datasets = [torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y)), torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))]
chain_dataset = torch.utils.data.ChainDataset(datasets)
print(chain_dataset)