input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
boundaries = torch.tensor([(- 0.5), 0.0, 0.5])
output = torch.bucketize(input_data, boundaries)