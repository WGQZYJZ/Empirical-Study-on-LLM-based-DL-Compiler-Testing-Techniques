input_data = torch.randn(2, 3, 4)
layer_norm = torch.nn.LayerNorm(input_data.size()[1:])
output = layer_norm(input_data)