input_data1 = torch.randn(1, 2, 3, 4)
input_data2 = torch.randn(1, 2, 3, 4)
output = torch.cat((input_data1, input_data2), dim=0)