
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3200, 1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v4  = torch.sigmoid(v1) * -56 + v1 
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(20, 3200)

