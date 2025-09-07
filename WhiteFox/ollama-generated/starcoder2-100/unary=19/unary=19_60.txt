
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48 * 48, 256)
 
    def forward(self, x1):
        v0 = torch.sigmoid(x1)
        return v0

# Initializing the model
m = Model()

