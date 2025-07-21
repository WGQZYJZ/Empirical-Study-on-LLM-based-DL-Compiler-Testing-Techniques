'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
import torch
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[10], [20], [30]])
ds = torch.utils.data.TensorDataset(torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32))
dl = torch.utils.data.DataLoader(ds, batch_size=2, shuffle=True)
for (x_batch, y_batch) in dl:
    print(x_batch)
    print(y_batch)
print(len(dl))