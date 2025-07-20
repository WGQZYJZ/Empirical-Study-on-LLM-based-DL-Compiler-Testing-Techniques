input_data = torch.randn(2, 3, 4)
output = torch.movedim(input_data, 0, 1)