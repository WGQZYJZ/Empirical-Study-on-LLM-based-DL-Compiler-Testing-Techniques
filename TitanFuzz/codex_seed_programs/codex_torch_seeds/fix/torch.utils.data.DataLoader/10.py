'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.DataLoader\ntorch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=2, persistent_workers=False)\n'
import torch
import numpy as np
import torch
x = np.random.rand(100, 1)
y = (((2 * x) + 3) + np.random.rand(100, 1))
torch_dataset = torch.utils.data.TensorDataset(torch.from_numpy(x).float(), torch.from_numpy(y).float())
loader = torch.utils.data.DataLoader(dataset=torch_dataset, batch_size=5, shuffle=True, num_workers=2)
for epoch in range(3):
    for (step, (batch_x, batch_y)) in enumerate(loader):
        print('Epoch: ', epoch, '| Step: ', step, '| batch x: ', batch_x.numpy(), '| batch y: ', batch_y.numpy())