'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
import torch.utils.data
import torch
X = torch.rand(10, 2)
y = torch.rand(10, 1)
dataloader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X, y), batch_size=4, shuffle=True, num_workers=4)
for (x_batch, y_batch) in dataloader:
    print(x_batch)
    print(y_batch)