

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(327680, 514)
    
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
        return v3


# Initializing the model and generate a valid input
m = Model()
x = torch.randn(50, 327680)
x[0].fill_(other_tensor / x[0][1])
x[49].fill_(torch.ones([32768]))
