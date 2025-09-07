
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = self.linear(x1) * negative_slope
        v3 = torch.where(v1, v1, v2)

        return v4


# Initializing the model and inputs to the model