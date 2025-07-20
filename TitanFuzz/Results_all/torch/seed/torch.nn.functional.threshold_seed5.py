input_data = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2]])
output_data = torch.nn.functional.threshold(input_data, threshold=0.5, value=0.0)