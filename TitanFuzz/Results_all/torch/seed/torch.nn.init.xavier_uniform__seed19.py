x = np.random.randn(3, 5)
x = torch.from_numpy(x)
torch.nn.init.xavier_uniform_(x)