x = torch.tensor(np.random.rand(1, 10, 10), dtype=torch.float32)
y = torch.nn.functional.tanh(x)