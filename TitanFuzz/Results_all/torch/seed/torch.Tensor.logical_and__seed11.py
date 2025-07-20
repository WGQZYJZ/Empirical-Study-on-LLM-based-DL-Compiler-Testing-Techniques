tensor_1 = torch.tensor([[False, False, False], [True, True, True], [False, False, False]])
tensor_2 = torch.tensor([[False, True, False], [False, True, False], [False, True, False]])
torch.Tensor.logical_and_(tensor_1, tensor_2)