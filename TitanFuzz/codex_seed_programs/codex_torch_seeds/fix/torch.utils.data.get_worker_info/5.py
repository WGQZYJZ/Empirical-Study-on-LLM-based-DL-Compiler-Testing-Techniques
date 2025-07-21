'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import torch.utils.data
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = torch.tensor([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
torch.utils.data.get_worker_info()