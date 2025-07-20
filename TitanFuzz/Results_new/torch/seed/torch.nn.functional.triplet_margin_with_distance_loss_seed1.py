anchor = torch.randn(1, 3, requires_grad=True)
positive = torch.randn(1, 3, requires_grad=True)
negative = torch.randn(1, 3, requires_grad=True)
loss = torch.nn.functional.triplet_margin_with_distance_loss(anchor, positive, negative)