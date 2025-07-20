data_size = 10
data_input = torch.randn(data_size, 3, 5)
data_output = torch.movedim(data_input, 2, 0)