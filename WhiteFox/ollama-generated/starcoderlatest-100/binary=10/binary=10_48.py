
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # Here the keyword argument "other" should be added to the output of linear transformation
        return v2


# Initializing the model
m2 = Model()


