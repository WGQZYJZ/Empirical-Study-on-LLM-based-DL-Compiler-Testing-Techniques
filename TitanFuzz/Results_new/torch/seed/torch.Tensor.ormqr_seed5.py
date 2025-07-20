input_data = torch.randn(3, 5, 4)
input2 = torch.randn(3, 5, 4)
input3 = torch.randn(3, 5, 4)
output_data = torch.Tensor.ormqr(input_data, input2, input3, left=True, transpose=False)