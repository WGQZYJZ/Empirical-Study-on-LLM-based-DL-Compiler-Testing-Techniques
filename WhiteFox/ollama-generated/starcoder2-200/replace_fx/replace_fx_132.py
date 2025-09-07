
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):

        v0 = torch.nn.functional.dropout(input=input1)
        t2 = torch.rand_like(v0).clamp_(min=0.5*2000, max=0.7*2000)
        return t2


m  = Model()
x1 = torch.randn(1, 320)

