
class Model(torch.nn.Module):
    def __init__(self, neg_slope=0.01):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 64)
        self.neg_slope = neg_slope
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32 * 32 * 3))
        v2 = v1 > 0
        v3 = v1 * self.neg_slope
        v4 = torch.where(v2, v1, v3)
        return v4
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
