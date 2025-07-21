'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
import torch.utils.data
print('PyTorch version: ', torch.__version__)
data = torch.randn(5, 3)
print(data)
loader = torch.utils.data.DataLoader(data, batch_size=2, shuffle=True, num_workers=2)
for (i, batch_data) in enumerate(loader):
    print(i, batch_data)