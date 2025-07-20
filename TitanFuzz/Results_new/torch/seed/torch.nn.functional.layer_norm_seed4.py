input_data = torch.randn(5, 5, dtype=torch.float32)
output = torch.nn.functional.layer_norm(input_data, [5], eps=1e-05)