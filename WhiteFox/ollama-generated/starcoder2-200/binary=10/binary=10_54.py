
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(v1.shape[0], v1.shape[-1])
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3, 30) 
 __output__  = m(x1)

