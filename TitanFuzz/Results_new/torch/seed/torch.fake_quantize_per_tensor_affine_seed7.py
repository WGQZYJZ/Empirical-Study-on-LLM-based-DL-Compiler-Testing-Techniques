input = torch.randn(3, 3).float()
quantized_tensor = torch.fake_quantize_per_tensor_affine(input, scale=0.5, zero_point=4, quant_min=0, quant_max=8)