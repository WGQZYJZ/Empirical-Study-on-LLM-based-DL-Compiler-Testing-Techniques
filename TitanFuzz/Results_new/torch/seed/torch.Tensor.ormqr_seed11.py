tensor_input_1 = torch.randn(2, 3, 3)
tensor_input_2 = torch.randn(3, 3)
tensor_input_3 = torch.randn(3, 3)
torch.Tensor.ormqr(tensor_input_1, tensor_input_2, tensor_input_3, left=True, transpose=False)