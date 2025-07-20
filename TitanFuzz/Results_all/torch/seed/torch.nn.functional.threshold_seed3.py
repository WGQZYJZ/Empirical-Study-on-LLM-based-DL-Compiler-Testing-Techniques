input_data = torch.rand(5, 3)
result = torch.nn.functional.threshold(input_data, 0.5, 0.1)