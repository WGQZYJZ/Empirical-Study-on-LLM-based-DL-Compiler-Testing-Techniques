input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
other = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = torch.Tensor.inner(input_tensor, other)