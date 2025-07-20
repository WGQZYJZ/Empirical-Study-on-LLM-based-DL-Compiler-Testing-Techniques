input_data = torch.randn(2, 3)
threshold_value = 0.5
threshold_module = torch.nn.Threshold(threshold_value, 0)
output_data = threshold_module(input_data)