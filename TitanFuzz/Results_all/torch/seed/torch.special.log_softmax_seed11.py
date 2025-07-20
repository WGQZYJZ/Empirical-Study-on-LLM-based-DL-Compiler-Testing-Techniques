input_data = torch.randn(3, 5)
output = torch.special.log_softmax(input_data, dim=1)