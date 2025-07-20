input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float32)
output_data = torch.nn.functional.mish(input_data)