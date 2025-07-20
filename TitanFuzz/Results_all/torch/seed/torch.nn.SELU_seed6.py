x = torch.tensor(np.random.rand(1, 2, 3, 4), dtype=torch.float32)
selu = torch.nn.SELU(inplace=False)
y = selu(x)