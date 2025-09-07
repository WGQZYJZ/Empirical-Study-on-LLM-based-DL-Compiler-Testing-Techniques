
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)

        v1_ = self.linear1(v1)
        v2_ = self.linear2(v2)

        t3 = torch.bmm(v1_, v2_)
        return t3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 3, 4)
