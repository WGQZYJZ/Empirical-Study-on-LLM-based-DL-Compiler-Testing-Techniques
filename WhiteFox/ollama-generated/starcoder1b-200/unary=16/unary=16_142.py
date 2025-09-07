
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return relu(v1)


# Initializing the model
m = Model()


