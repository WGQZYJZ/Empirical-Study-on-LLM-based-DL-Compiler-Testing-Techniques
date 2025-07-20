input_tensor = torch.randn(3, 5)
input2 = torch.randn(5, 2)
input3 = torch.randn(5, 2)
output = torch.Tensor.ormqr(input_tensor, input2, input3, left=True, transpose=False)