inp_tensor = torch.Tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
torch.Tensor.put_(inp_tensor, [0, 1, 2, 3, 4, 5, 6, 7, 8], [11, 22, 33, 44, 55, 66, 77, 88, 99])
torch.Tensor.put_(inp_tensor, [0, 1, 2, 3, 4, 5, 6, 7, 8], [11, 22, 33, 44, 55, 66, 77, 88, 99], accumulate=True)