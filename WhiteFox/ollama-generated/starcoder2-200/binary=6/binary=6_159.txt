
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)

    def forward(self, x):
       v1 = self.linear(x) 
       v2 = v1 - other
       return v2

# Initializing the model
m = Model()
other = torch.randn([1]).detach().requires_grad_(True)

# Inputs to the model 
x = torch.randn(8, requires_grad=True)
__output__  = m(x)

