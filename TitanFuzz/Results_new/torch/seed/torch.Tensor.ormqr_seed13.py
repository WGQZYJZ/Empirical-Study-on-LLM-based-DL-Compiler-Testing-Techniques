input_tensor = torch.rand(2, 3, 4)
input2 = torch.rand(2, 3, 4)
input3 = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.ormqr(input_tensor, input2, input3, left=True, transpose=False)