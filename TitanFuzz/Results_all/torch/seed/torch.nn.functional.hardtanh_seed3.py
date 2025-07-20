input_data = np.random.uniform(low=(- 2), high=2, size=(2, 3))
input_data = torch.from_numpy(input_data)
output_data = torch.nn.functional.hardtanh(input_data, min_val=(- 1.0), max_val=1.0)