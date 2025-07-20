input_size = (2, 3, 4)
input_data = torch.randn(input_size)
layer_norm = torch.nn.LayerNorm(input_size[1:])
output = layer_norm(input_data)