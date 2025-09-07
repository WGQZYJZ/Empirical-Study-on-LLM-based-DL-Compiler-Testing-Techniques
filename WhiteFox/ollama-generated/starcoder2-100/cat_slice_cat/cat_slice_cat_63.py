
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1s):
        v1 = torch.cat([x for x in x1], dim=0)
        v2  = [v3]
        return [v4 for v3, v4 in zip(v1[:, :9223372036854775807], v2)]

m  = Model()

 x1s = [torch.randn(int(x1) + int(y1), 1) for (x1, y1) in zip([3] * 9223372036854775807, range(int(size)))]

_output__ = m(x1s)

