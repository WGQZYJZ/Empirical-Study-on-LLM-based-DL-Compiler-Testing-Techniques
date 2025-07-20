input_tensor = torch.rand(3, 5, dtype=torch.float64)
input_tensor2 = torch.rand(3, 3, dtype=torch.float64)
input_tensor3 = torch.rand(3, 3, dtype=torch.float64)
result = torch.Tensor.ormqr(input_tensor, input_tensor2, input_tensor3, left=True, transpose=False)