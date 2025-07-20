input_data = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]], dtype=torch.float32)
output_data = torch.nn.functional.selu(input_data)