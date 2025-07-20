input_data = torch.randn(2, 2)
threshold = 0.5
value = (- 1)
output = torch.nn.functional.threshold(input_data, threshold, value)