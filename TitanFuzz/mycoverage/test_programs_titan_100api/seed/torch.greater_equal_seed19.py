input_data = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]], dtype=torch.float)
other_data = torch.tensor([[1, 2, 3], [(- 1), (- 2), (- 3)]], dtype=torch.float)
output_data = torch.greater_equal(input_data, other_data)