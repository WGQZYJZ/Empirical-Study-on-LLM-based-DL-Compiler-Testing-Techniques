input_data = torch.randn(20, 5, 10)
norm_layer = torch.nn.LayerNorm(input_data.size()[1:])
output = norm_layer(input_data)
output = layer_norm(input_data, input_data.size()[1:])