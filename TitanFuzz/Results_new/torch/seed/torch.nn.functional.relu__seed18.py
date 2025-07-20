input_data = torch.tensor([(- 1.0), 1.0, 3.0, 5.0])
output_data = torch.nn.functional.relu_(input_data)
assert torch.equal(output_data, torch.tensor([0.0, 1.0, 3.0, 5.0]))