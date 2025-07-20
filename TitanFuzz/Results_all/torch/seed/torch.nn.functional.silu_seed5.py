input_data = np.array([[(- 1.0), (- 2.0), (- 3.0)], [1.0, 2.0, 3.0]])
input = torch.from_numpy(input_data)
output = torch.nn.functional.silu(input)