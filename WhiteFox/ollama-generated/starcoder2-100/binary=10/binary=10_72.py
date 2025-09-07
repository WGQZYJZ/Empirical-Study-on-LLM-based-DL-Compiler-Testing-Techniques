
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        return 0.75 * torch.relu(v1)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32) 
