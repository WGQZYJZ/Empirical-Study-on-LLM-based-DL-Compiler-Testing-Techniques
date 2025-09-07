
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(0.2, requires_grad=True)
 
    def forward(self, key, value):
        q  = torch.randn(300)
        v1  = torch.nn.functional.linear(q, k, bias=None).div(self.scale)
        v2  = v1.softmax(-1).mul(v1, -1).div(v1.sum(-1))
