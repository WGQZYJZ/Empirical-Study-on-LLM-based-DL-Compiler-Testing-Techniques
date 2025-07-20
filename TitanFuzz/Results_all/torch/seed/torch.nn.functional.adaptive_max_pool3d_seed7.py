input = torch.randn(1, 16, 10, 10, 10)
(output, indices) = torch.nn.functional.adaptive_max_pool3d(input, (5, 5, 5), return_indices=True)
input = torch.randn(1, 16, 10, 10, 10)