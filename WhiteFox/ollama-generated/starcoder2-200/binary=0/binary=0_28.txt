
class Model(torch.nn.Module):
    def __init__(self, constant):
        super().__init__()
        self.constant = constant # This value can be different from zero in some cases
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.constant # The value of constant is different from zero in some cases
        return v2

# Initializing the model with a constant other than zero (in most of cases)
m0, m1 = Model(other=torch.tensor(45)), Model(other=torch.tensor(-3))

