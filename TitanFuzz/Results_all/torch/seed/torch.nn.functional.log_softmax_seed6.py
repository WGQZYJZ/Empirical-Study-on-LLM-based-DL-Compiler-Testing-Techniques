input_data = torch.randn(2, 3)
output = torch.nn.functional.log_softmax(input_data, dim=1)