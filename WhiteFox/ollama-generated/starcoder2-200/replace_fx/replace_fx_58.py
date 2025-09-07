
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, torch.zeros([1])) 
        return v2

m  = Model()
x1 = torch.randn(3)

