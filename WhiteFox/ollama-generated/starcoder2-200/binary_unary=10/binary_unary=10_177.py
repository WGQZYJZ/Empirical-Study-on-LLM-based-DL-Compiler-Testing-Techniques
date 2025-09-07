
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = v1 + torch.randn_like(v1) 
        v5  = relu(v4)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model