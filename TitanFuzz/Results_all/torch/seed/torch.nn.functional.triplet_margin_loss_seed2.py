data_size = 32
anchor = np.random.rand(data_size, 3, 32, 32).astype(np.float32)
positive = np.random.rand(data_size, 3, 32, 32).astype(np.float32)
negative = np.random.rand(data_size, 3, 32, 32).astype(np.float32)
anchor = torch.from_numpy(anchor)
positive = torch.from_numpy(positive)
negative = torch.from_numpy(negative)
output = torch.nn.functional.triplet_margin_loss(anchor, positive, negative, margin=1.0, p=2, eps=1e-06, swap=False, size_average=None, reduce=None, reduction='mean')