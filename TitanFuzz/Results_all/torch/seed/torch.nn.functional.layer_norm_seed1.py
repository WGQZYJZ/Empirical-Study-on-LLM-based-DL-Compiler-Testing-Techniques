input_data = torch.randn(3, 4, 5)
output = torch.nn.functional.layer_norm(input_data, normalized_shape=(4, 5))