np.random.seed(42)
input = np.random.randn(10, 10).astype(np.float32)
input = torch.from_numpy(input)
output = torch.nn.functional.rrelu(input)