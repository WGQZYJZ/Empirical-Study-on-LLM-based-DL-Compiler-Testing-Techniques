input_data = torch.randn(2, 3)
input_data_real = torch.randn(2, 3, dtype=torch.float)
input_data_complex = torch.randn(2, 3, dtype=torch.complex64)
torch.isreal(input_data)
torch.isreal(input_data_real)
torch.isreal(input_data_complex)