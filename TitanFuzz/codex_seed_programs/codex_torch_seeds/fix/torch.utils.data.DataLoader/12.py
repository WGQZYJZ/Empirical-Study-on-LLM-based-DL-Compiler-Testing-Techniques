'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
from torch.utils.data import DataLoader
import torch
from torch.utils.data import DataLoader
x = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.Tensor([[1], [2], [3]])
dataloader = DataLoader(dataset=list(zip(x, y)), batch_size=2, shuffle=True)
for (batch_x, batch_y) in dataloader:
    print(batch_x)
    print(batch_y)
    print(('=' * 20))