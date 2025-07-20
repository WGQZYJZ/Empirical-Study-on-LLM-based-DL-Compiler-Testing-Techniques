x = np.random.rand(100, 3)
y = np.random.randint(0, 2, (100,))
dataset = torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))