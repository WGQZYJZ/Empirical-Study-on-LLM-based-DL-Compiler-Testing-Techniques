
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
        self.other  = nn.Parameter(torch.randn([8192]))
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 512)
__output__  = m(x1)