input_data = torch.rand(size=(2, 3))
trans = torch.distributions.transforms.ReshapeTransform(in_shape=(2, 3), out_shape=(3, 2))
output = trans(input_data)