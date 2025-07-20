input_data = torch.randn(3, 3)
input_data = torch.randn(3, 3)
output = torch.linalg.cholesky_ex(input_data, upper=False, check_errors=False)
input_data = torch.randn(3, 3)