input = torch.randn(1, 64, 8)
output = torch.nn.AdaptiveMaxPool1d(4)(input)
(output, indices) = torch.nn.AdaptiveMaxPool1d(4, return_indices=True)(input)