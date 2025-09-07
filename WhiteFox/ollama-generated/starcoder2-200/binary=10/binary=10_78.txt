
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*10, 4)
 
    def forward(self, x1):
         v1 = self.linear(x1) + torch.randn(v1.shape[-2:])
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model