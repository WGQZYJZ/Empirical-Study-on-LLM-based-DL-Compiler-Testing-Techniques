input_tensor = torch.randn(2, 3, 4)
input2 = torch.randn(2, 3, 4)
output = torch.Tensor.orgqr(input_tensor, input2)