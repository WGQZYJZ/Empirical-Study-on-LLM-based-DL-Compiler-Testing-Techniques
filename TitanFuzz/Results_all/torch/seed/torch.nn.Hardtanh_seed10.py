input_data = Variable(torch.Tensor([[(- 1.0), (- 0.5), 0.0, 1.0, 2.0]]))
input_data = Variable(torch.Tensor([[(- 1.0), (- 0.5), 0.0, 1.0, 2.0]]))
hardtanh = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)
output = hardtanh(input_data)