input_data = torch.randn(1, 2, 3)
threshold = torch.nn.Threshold(0.5, 0)
output_data = threshold(input_data)