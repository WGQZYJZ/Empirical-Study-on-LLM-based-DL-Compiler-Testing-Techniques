x = torch.randn(100, 3)
y = torch.randn(100, 2)
dataset = torch.utils.data.TensorDataset(x, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=10, shuffle=True)
for (i, (x, y)) in enumerate(dataloader):
    print(i, x.size(), y.size())
dataset = torch.utils.data.TensorDataset(x, y)
dataloader = torch.utils