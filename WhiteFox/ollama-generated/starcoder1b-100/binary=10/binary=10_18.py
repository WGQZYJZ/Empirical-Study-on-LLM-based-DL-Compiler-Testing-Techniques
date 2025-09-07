
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m2 = Model2()

