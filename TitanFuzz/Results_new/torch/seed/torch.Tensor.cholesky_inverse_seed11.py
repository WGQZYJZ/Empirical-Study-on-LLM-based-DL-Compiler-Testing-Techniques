input_tensor = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
result = torch.Tensor.cholesky_inverse(input_tensor, upper=False)