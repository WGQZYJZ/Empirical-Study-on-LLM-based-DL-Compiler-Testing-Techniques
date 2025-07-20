input = torch.randn(2, 3, 4, 5)
output = torch.nn.functional.layer_norm(input, [3, 4, 5])