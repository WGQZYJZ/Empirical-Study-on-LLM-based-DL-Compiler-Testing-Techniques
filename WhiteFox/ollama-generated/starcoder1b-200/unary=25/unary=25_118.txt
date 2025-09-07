
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = (t1 > 0).float()
        t3 = t1 * self.negative_slope
        t4 = torch.where(t2, t1, t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
