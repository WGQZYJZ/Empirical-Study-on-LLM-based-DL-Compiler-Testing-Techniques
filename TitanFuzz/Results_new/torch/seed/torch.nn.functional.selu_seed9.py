input_data = torch.tensor([[(- 1), 0, 1], [2, 3, 4]], dtype=torch.float)
output_data = torch.nn.functional.selu(input_data)