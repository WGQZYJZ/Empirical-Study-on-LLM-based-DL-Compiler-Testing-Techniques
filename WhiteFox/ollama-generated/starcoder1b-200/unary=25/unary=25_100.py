
class Model(torch.nn.Module):
    def __init__(self, alpha):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
        self.alpha = alpha
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.alpha
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model(alpha=0.5)


