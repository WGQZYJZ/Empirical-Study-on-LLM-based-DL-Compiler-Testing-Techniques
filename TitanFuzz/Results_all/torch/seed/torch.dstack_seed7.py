input_tensor_1 = torch.randn(2, 3, 4)
input_tensor_2 = torch.randn(2, 3, 4)
output_tensor = torch.dstack((input_tensor_1, input_tensor_2))