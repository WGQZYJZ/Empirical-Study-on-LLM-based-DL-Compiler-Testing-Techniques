input_data = torch.arange(0, 10, dtype=torch.float)
scale = 1
zero_point = 0
quant_min = 0
quant_max = 10
quantized_tensor = torch.fake_quantize_per_tensor_affine(input_data, scale, zero_point, quant_min, quant_max)
quantization_error = (quantized_tensor - input_data)