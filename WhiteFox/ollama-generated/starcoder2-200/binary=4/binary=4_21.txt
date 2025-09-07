
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + torch.randn_like(v1).to("cuda")


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn((32,), device="cuda")

__output__  = m(x1)