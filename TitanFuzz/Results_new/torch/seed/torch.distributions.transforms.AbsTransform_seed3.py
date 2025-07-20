input_data = torch.randn(3, 4)
abs_transform = torch.distributions.transforms.AbsTransform()
output_data = abs_transform(input_data)