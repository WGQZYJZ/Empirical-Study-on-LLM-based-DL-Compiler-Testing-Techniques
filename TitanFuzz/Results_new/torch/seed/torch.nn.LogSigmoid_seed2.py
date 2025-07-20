input_data = torch.tensor([[(- 1.0), (- 2.0), (- 3.0)], [1.0, 2.0, 3.0]])
output_data = torch.nn.LogSigmoid()(input_data)
output_data = torch.sigmoid(input_data)