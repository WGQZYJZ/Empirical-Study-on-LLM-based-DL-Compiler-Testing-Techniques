input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, 5).random_(2)
output = torch.nn.functional.multilabel_soft_margin_loss(input, target)