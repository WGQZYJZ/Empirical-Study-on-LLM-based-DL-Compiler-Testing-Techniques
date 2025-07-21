'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
from torch.utils.data import DataLoader
import torch
from torch.utils.data import DataLoader
input_data = torch.randn(10, 3)
data_loader = DataLoader(input_data, batch_size=2, shuffle=False)
for batch_data in data_loader:
    print(batch_data)
data_loader = DataLoader(input_data, batch_size=2, shuffle=True)
for batch_data in data_loader:
    print(batch_data)