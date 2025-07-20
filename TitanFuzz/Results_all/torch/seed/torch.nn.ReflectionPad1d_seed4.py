input_data = torch.arange(1, 9, dtype=torch.float).view(1, 2, 4)
reflection_pad = torch.nn.ReflectionPad1d(2)
output_data = reflection_pad(input_data)