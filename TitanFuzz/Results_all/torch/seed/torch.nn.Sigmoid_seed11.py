input_data = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
output_data = torch.nn.Sigmoid()(input_data)