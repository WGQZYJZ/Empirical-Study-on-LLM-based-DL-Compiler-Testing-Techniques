x = torch.rand(1, 3, 224, 224)
x = torch.jit.annotate(torch.Tensor, x)