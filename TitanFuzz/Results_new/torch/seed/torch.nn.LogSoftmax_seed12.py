input_data = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float)
output_data = torch.nn.LogSoftmax(dim=1)(input_data)