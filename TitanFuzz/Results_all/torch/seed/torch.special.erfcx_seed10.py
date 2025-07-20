input_data = torch.tensor(np.random.rand(1, 2, 3, 4), dtype=torch.double)
output = torch.special.erfcx(input_data)