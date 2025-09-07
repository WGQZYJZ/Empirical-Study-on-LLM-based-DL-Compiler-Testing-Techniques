
class Model(torch.nn.Module):
    def __init__(self, num1):
        super().__init__()

    def forward(self, input):
        v1 = torch.addmm(input, num1) # Input 1
        v2 = torch.cat([v1], dim=0)   # Input 2
        return v2

m = Model()

