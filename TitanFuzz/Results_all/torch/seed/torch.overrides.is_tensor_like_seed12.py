input_data = [1, 2, 3, 4, 5]
is_tensor_like = torch.overrides.is_tensor_like(input_data)
input_data = torch.tensor(input_data)
is_tensor_like = torch.overrides.is_tensor_like(input_data)
input_data = torch.randn(3, 3)
is_tensor_like = torch.overrides.is_tensor_like(input_data)