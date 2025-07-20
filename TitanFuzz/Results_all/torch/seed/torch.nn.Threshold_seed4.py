input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
threshold = torch.nn.Threshold(0.0, 0.0)
output = threshold(input_data)