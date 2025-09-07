
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() 
        v3 = negative_slope * v1
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model()
negative_slope=torch.randn([8])

# Inputs to the model
x1  = torch.randn([8, 32], requires_grad=True)
__output__  = m(x1)


