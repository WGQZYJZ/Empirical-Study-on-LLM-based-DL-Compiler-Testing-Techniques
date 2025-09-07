
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x):
        w  = self.linear(x)
        return torch.where(w > 0, w, -w * 2)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
