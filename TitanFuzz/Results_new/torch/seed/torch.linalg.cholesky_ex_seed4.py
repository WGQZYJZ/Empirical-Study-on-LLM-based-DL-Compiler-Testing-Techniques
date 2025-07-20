input_data = torch.tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]], dtype=torch.float)
output = torch.linalg.cholesky_ex(input_data, upper=False)