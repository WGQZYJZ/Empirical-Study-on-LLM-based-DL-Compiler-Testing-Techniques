
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 350)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other 
        return nn.ReLU()(v2).float()


# Initializing the model
m  = Model()
