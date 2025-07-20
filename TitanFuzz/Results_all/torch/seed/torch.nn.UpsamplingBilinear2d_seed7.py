input_data = torch.tensor(np.random.rand(1, 1, 4, 4), dtype=torch.float32)
output = torch.nn.UpsamplingBilinear2d(size=None, scale_factor=2)(input_data)
input_data = torch.tensor(np.random.rand(1, 1, 4, 4), dtype=torch.float32)
output = torch.nn.UpsamplingNearest2d(size=None, scale_factor=2)(input_data)