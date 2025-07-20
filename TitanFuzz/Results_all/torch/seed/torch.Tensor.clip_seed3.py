input_tensor = torch.randn([1, 3, 224, 224])
output_tensor = torch.Tensor.clip(input_tensor, min=0.0, max=1.0)