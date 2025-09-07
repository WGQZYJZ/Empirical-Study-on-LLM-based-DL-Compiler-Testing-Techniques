
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 128, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1e-6  # Subtract a small constant from the output of the linear transformation
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


