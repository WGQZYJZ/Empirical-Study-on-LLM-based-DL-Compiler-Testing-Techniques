import torch
from torch import nn
from torch.autograd import Variable
x = np.random.rand(100, 1)
y = (((2 * x) + 5) + np.random.rand(100, 1))
x_tensor = torch.from_numpy(x).float()
y_tensor = torch.from_numpy(y).float()
dataset = torch.utils.data.TensorDataset(x_tensor, y_tensor)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)
model = torch.nn.Linear(1, 1)