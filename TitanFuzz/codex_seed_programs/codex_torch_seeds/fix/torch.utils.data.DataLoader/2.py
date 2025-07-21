'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('CUDA available: ', torch.cuda.is_available())
print('')
print('Task 2: Generate input data')
input_data = torch.randn(5, 3)
print('input_data: ', input_data)
print('')
print('Task 3: Call the API torch.utils.data.DataLoader')
dataloader = torch.utils.data.DataLoader(input_data, batch_size=2, shuffle=True)
for (batch_idx, batch_data) in enumerate(dataloader):
    print('batch_idx: ', batch_idx)
    print('batch_data: ', batch_data)
    print('')