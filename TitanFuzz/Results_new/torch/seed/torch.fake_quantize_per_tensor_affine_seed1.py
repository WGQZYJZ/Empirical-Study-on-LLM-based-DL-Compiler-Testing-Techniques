input = torch.rand(1, 2, 3, dtype=torch.float)
quantized_input = torch.fake_quantize_per_tensor_affine(input, scale=1.0, zero_point=0, quant_min=0, quant_max=255)