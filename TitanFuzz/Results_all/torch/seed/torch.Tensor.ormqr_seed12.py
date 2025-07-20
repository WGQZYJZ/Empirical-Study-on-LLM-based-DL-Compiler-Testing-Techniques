input_tensor = torch.randn(2, 3, 4)
input_tensor2 = torch.randn(2, 3, 4)
input_tensor3 = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.ormqr(input_tensor, input_tensor2, input_tensor3, left=True, transpose=False)