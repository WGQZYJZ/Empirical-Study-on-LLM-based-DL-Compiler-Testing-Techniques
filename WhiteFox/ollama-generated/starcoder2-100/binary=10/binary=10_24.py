
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x2):
         v1  = self.linear(x2)
         v2  = v1 + other # <|>
         return v2


# Initializing the model
m = Model()
other = torch.randn(10,)


# Inputs to the model
x2 = torch.randn(5, 32, 10)
__output__  = m(x2)

