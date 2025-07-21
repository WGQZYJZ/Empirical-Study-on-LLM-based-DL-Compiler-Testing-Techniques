'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
x = np.random.rand(100, 1)
y = (((2 * x) + 5) + np.random.rand(100, 1))
x_tensor = torch.from_numpy(x).float()
y_tensor = torch.from_numpy(y).float()
dataset = torch.utils.data.TensorDataset(x_tensor, y_tensor)
print(dataset)
'\nTask 1: Create a DataLoader\nTask 2: Set batch_size = 4\nTask 3: Set shuffle = True\nTask 4: Set num_workers = 2\n'
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)
print(dataloader)
'\nTask 1: Create a linear regression model\nTask 2: Set the input dimension to 1\nTask 3: Set the output dimension to 1\n'
model = torch.nn.Linear(1, 1)
print(model)