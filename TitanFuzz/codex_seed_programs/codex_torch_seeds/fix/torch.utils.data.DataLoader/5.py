'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
import torch
x = torch.randn(100, 10)
y = torch.randint(0, 10, (100,))
dataloader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(x, y), batch_size=32, shuffle=True)
for (x, y) in dataloader:
    print(x.shape, y.shape)