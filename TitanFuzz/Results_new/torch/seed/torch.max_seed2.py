input = torch.randn(3, 5)
(max_value, max_idx) = torch.max(input, dim=0)
(max_value, max_idx) = torch.max(input, dim=1)