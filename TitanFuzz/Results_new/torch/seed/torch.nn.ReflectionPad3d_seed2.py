input_data = torch.randn(1, 1, 3, 3, 3)
reflection_pad3d = torch.nn.ReflectionPad3d(padding=(1, 1, 1, 1, 1, 1))
output_data = reflection_pad3d(input_data)