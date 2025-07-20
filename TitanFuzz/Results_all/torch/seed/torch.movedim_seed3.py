input_data = torch.randn(3, 4, 5)
output_data = torch.movedim(input_data, 0, (- 1))