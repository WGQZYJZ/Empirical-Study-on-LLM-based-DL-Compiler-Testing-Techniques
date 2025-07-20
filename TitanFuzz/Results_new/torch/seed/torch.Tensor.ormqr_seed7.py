input_tensor = torch.randn(3, 5, 10, 10)
input2 = torch.randn(3, 5, 10, 10)
input3 = torch.randn(3, 5, 10, 10)
output = torch.Tensor.ormqr(input_tensor, input2, input3, left=True, transpose=False)