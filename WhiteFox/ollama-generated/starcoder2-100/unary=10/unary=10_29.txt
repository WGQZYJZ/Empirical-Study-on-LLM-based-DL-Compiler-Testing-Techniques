
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 1)
 
    def forward(self, x):
        y = self.linear(x)
        return torch.clamp_min(y + 3 , 0),torch.clamp_max(torch.ceil(y /6), 6),x


# Initializing the model
m = Model()

# Inputs to the model
x1= torch.rand((5,))


