'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import torch.utils.data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=True, num_workers=1)
for (i, batch) in enumerate(loader):
    print(i, batch)
    print(torch.utils.data.get_worker_info())