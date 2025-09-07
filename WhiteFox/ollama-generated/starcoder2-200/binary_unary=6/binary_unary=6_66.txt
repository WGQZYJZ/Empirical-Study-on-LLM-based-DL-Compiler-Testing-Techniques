
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 7)
        self.linear2 = torch.nn.Linear(6, 3)
        self.activation = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(v1)
        v3 = self.activation(v2 - other)
        return v3

# Initializing the model
m  = Model2()


# Inputs to the model
x  = torch.randn(7, 5) # Input tensor of size 7 X 5
other  = x.mean()
__output__  = m(x)

