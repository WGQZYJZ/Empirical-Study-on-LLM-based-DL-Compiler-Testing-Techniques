'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import torch.utils.data
x = torch.randn(10, 1)
y = torch.randn(10, 1)
train_sampler = torch.utils.data.SubsetRandomSampler(indices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
train_loader = torch.utils.data.DataLoader(dataset=torch.utils.data.TensorDataset(x, y), batch_size=2, sampler=train_sampler)
for (batch_idx, (x_batch, y_batch)) in enumerate(train_loader):
    print(batch_idx, x_batch, y_batch)