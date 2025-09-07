
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other  # Here `other` is another tensor 
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model