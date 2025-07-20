input_data = torch.randn(3, 3)
scale = 1.0
zero_point = 0
quant_min = 0
quant_max = 255
quantized_data = torch.fake_quantize_per_tensor_affine(input_data, scale, zero_point, quant_min, quant_max)