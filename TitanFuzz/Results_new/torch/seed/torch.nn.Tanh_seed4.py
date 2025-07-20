input_data = torch.tensor([[(- 1.0), (- 2.0), (- 3.0)], [1.0, 2.0, 3.0]])
tanh_output = torch.nn.Tanh()
output = tanh_output.forward(input_data)