data = torch.randn(2, 3, 4)
reshape = torch.distributions.transforms.ReshapeTransform((2, 3, 4), (3, 8))