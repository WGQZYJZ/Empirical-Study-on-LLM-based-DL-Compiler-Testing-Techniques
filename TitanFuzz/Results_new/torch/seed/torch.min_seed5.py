input = torch.randn(3, 4)
(min_value, min_index) = torch.min(input, dim=1)