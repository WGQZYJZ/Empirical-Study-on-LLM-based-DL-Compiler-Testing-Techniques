input = np.random.randn(4, 4)
input = torch.from_numpy(input)
torch.isnan(input)