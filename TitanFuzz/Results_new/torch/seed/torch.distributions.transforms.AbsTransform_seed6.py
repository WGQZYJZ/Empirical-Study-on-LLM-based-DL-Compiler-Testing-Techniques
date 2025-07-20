x = torch.randn(3, 4)
abs_transform = torch.distributions.transforms.AbsTransform()
abs_transform(x)