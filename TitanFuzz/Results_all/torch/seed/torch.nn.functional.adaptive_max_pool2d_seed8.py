input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.adaptive_max_pool2d(input, (3, 3))
(output, indices) = torch.nn.functional.adaptive_max_pool2d(input, (3, 3), return_indices=True)