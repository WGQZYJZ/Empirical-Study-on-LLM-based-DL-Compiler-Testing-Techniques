input_data = torch.randn(1, 1, 3, 3)
elu = torch.nn.ELU()
output = elu(input_data)
input_data = torch.randn(1, 1, 3, 3)
hardshrink = torch.nn.Hardshrink()
output = hardshrink(input_data)
input_data = torch