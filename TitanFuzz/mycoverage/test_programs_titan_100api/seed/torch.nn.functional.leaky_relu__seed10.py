input_data = torch.tensor(np.random.rand(10, 10), dtype=torch.float)
output_data = torch.nn.functional.leaky_relu_(input_data)