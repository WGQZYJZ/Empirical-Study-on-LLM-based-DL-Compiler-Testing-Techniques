input_data1 = torch.randn(3, 3)
input_data2 = torch.randn(3, 3)
input_data3 = torch.randn(3, 3)
result = torch.linalg.multi_dot([input_data1, input_data2, input_data3])