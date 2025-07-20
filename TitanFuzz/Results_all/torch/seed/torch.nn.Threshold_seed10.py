input_data = torch.tensor([[1, (- 1), 1], [(- 1), 1, (- 1)], [1, 1, 1], [(- 1), (- 1), (- 1)]], dtype=torch.float)
threshold = torch.nn.Threshold(0.0, 0.0)
output = threshold(input_data)