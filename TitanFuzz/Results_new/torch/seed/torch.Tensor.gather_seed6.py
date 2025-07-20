input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([[0, 1], [1, 2], [2, 0]]))