
class Model(torch.nn.Module):
    def __init__(self, other=3.14):
        super().__init__()
        self.linear = torch.nn.Linear(6, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (torch.randn_like(v1)*other).sin() # Apply a random sign to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

