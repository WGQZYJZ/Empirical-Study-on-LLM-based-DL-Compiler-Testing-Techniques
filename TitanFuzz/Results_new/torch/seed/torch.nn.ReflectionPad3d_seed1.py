x = torch.randn(1, 1, 3, 3, 3)
reflection_pad = torch.nn.ReflectionPad3d((1, 1, 1, 1, 1, 1))
y = reflection_pad(x)