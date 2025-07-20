input_data = torch.tensor([[1.0, (- 1.0), 0.0], [0.0, 0.0, 0.0]])
output = torch.nn.LogSigmoid()(input_data)