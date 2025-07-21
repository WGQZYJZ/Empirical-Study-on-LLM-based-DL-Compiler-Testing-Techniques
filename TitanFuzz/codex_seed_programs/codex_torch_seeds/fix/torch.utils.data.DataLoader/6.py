'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
input_data = torch.rand(10, 3)
target_data = torch.rand(10)
dataset = torch.utils.data.TensorDataset(input_data, target_data)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True)
for (batch_index, (input_data, target_data)) in enumerate(dataloader):
    print('batch_index: ', batch_index)
    print('input_data: ', input_data)
    print('target_data: ', target_data)
    print('\n')