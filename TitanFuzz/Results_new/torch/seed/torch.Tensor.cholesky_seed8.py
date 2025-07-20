input_tensor = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
cholesky = torch.Tensor.cholesky(input_tensor, upper=False)