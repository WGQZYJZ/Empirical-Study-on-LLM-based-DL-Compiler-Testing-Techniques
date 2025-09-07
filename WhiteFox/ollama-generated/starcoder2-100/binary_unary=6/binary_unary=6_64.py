
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20,13)
 
    def forward(self, x1):
        v1 =  other
        v2 = self.linear(x1) - v1
        v4 = F.relu(v2)
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1= torch.randn(1, 60)
