input_data = torch.tensor([0, 0.5, 1], dtype=torch.float)
output_data = torch.arccos(input_data)
expected_output = torch.tensor([(math.pi / 2), (math.pi / 3), 0], dtype=torch.float)
diff = (expected_output - output_data)
max_diff = torch.max(diff).item()
if (max_diff < 1e-06):
    print('Correct')
else:
    print('Incorrect')