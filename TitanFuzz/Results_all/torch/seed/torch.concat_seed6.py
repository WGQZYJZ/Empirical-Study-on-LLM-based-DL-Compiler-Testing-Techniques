tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
tensor_concat_1 = torch.concat((tensor_1, tensor_2), dim=0)
tensor_concat_2 = torch.concat((tensor_1, tensor_2), dim=1)