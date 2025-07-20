input_data = torch.arange(1, 10, dtype=torch.float).view(1, 1, 9)
reflection_pad1d = torch.nn.ReflectionPad1d(2)
output = reflection_pad1d(input_data)