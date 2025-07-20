input = torch.randn(1, 1, 10, 10)
output = torch.nn.functional.adaptive_max_pool2d(input, (4, 4))
(output, indices) = torch.nn.functional.adaptive_max_pool2d(input, (4, 4), return_indices=True)