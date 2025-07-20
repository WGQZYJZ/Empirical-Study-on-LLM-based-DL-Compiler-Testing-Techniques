input_data = torch.randn(2, 3, dtype=torch.float)
output_data = torch.Tensor.is_inference(input_data)