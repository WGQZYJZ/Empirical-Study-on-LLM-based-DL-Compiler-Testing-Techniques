input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 1, 2])
result = torch.Tensor.gather(input_tensor, 1, index)