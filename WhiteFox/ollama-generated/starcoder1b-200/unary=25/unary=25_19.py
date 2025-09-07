
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.gt(t1, 0)
        t3 = negative_slope * t1
        t4 = torch.where(t2, t1, t3)
        return t4


# Initializing the model
m = Model()


