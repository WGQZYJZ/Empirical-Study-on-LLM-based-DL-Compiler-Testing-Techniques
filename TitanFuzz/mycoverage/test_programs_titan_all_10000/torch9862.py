import torch
from torch import nn
from torch.autograd import Variable
data = np.random.rand(10, 3)
torch.utils.data.get_worker_info()
dataset = torch.utils.data.TensorDataset(torch.from_numpy(data))
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2)
for (i, batch) in enumerate(dataloader):
    print(torch.utils.data.get_worker_info())