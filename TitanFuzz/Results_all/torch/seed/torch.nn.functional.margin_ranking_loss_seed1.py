input1 = torch.randn(100, requires_grad=True)
input2 = torch.randn(100, requires_grad=True)
target = torch.empty(100).random_(2)
loss = torch.nn.functional.margin_ranking_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')