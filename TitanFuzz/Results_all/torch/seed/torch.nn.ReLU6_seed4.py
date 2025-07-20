input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0], dtype=torch.float)
relu6 = torch.nn.ReLU6()
output = relu6(input_data)