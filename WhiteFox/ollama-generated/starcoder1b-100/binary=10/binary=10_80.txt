
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 512)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
__input__  = torch.randn(1, 2048)
other = torch.randn(512)
