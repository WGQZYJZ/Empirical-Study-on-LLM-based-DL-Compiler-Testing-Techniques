x = torch.randn(100, 10)
y = torch.randint(0, 10, (100,))
dataloader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(x, y), batch_size=32, shuffle=True)
for (x, y) in dataloader:
    print(x.shape, y.shape)