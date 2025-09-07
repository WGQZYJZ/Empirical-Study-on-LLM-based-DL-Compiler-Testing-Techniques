
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 24 * 24, 10)
 
    def forward(self, x):
        x = x.view(x.size(0), -1)  # flatten x
        x = self.linear(x)  # calculate z
        return x


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 8 * 24 * 24)
