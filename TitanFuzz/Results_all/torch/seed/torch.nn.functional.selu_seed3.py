x_data = np.random.randn(2, 3)
x = torch.tensor(x_data, dtype=torch.float)
y = torch.nn.functional.selu(x)