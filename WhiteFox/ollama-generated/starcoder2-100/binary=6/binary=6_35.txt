
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7, 10)
 
    def forward(self, x):
        y = self.linear(x) - v3 # where 'v3' is another tensor or a constant
        return y

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(7)
__output__  = m(x)