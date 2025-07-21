'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
input_data = torch.randn(1000, 10)
print(torch.utils.data.get_worker_info())