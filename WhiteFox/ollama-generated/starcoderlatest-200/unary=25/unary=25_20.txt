
class Model(torch.nn.Module):
    def __init__(self, neg_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        negative_slope = torch.tensor(-neg_slope)
        t2 = v1 > 0
        v3 = v1 * negative_slope
        t4 = torch.where(t2, v1, v3)
        return t4


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 64)
