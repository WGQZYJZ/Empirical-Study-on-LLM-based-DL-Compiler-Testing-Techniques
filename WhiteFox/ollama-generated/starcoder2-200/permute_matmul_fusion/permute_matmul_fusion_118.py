class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        t2 = torch.randn(3, 4)
        t3 = t1 + self.linear0.weight[None].transpose(-1, -2)

        t6 = t2 @ (t3 * t5).sum(dim=2)[-2:, :, None]
        
        t7 = t6.permute([1, 2, 0])

        return [t7], t4, t8
