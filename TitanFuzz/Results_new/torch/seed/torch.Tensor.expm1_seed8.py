input_data = np.random.rand(10, 10)
input_tensor = torch.tensor(input_data)
output_tensor = torch.Tensor.expm1(input_tensor)
output_tensor = torch.expm1(input_tensor)