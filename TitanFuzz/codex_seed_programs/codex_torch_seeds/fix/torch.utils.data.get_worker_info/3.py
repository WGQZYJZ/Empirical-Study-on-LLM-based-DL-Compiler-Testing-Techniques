'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import numpy as np
import torch
import numpy as np
data = np.random.rand(10, 3)
torch.utils.data.get_worker_info()
dataset = torch.utils.data.TensorDataset(torch.from_numpy(data))
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2)
for (i, batch) in enumerate(dataloader):
    print(torch.utils.data.get_worker_info())