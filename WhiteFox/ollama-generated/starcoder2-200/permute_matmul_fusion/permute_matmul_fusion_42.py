
class Model(torch.nn.Module):
    def __init__(self, n1=2048):
        super().__init__()

        self._n1 = n1

    def forward(self, t1, t2):
        t3  = torch.bmm(t1.permute(0, 2, 1), t2) 
        return t3

# Initializing the model
m  = Model()

# Inputs to the model
i1  = torch.randn(8, 64, 375).cuda()
i2  = torch.randn(8, 64, 500).cuda()

