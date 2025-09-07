
class Model(torch.nn.Module):
    def __init__(self, t2=0):
        super().__init__()

    def forward(self, t1):
        t3  = torch.bmm(t1.permute(0, 2, 1), self.t2)
        return t3


# Initializing the model