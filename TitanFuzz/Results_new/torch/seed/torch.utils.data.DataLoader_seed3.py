x = np.random.rand(100, 1)
y = (((2 * x) + 3) + np.random.rand(100, 1))
torch_dataset = torch.utils.data.TensorDataset(torch.from_numpy(x).float(), torch.from_numpy(y).float())
loader = torch.utils.data.DataLoader(dataset=torch_dataset, batch_size=5, shuffle=True, num_workers=2)
for epoch in range(3):
    for (step, (batch_x, batch_y)) in enumerate(loader):
        print('Epoch: ', epoch, '| Step: ', step, '| batch x: ', batch_x.numpy(), '| batch y: ', batch_y.numpy())