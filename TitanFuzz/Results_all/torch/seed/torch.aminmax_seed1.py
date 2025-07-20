input_data = torch.randn(3, 4)
(min_value, max_value) = torch.aminmax(input_data, dim=1, keepdim=True)