input_data = torch.tensor([[(- 1), (- 0.5), 0, 0.5, 1]], dtype=torch.float32)
threshold = 0
value = 0
output_data = torch.nn.functional.threshold(input_data, threshold, value)