
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features=8, out_features=32)
 
    def forward(self, x1):
        v1  = x1 * torch.randn(x1.shape[0], x1.shape[1] + 3)
        v2  = self.fc1(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 8)
