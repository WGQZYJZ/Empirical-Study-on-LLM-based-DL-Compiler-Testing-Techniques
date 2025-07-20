input_data = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
sigmoid = torch.nn.Sigmoid()
output = sigmoid(input_data)