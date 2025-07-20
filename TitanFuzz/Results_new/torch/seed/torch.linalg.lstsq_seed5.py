features = torch.randn((1, 3))
labels = torch.randn((1, 1))
weights = torch.linalg.lstsq(features, labels)