'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
import torch.utils.data as data
import torch
import torch.utils.data as data
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_loader = data.DataLoader(input_data, batch_size=2, shuffle=True)
for batch_data in data_loader:
    print(batch_data)