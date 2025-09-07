
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 4)
 
    def forward(self, x1):
        v0 = F.normalize(x1)
        v3 = torch.sigmoid(v0[:, :])
        return v3

# Initializing the model
m = Model()


# Inputs to the model