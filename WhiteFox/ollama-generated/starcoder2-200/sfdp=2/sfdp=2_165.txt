
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1, padding=1)
 
    def forward(self, x1):
        v0  = torch.nn.functional.dropout(x1, p=0.5)
        v1  = v0 * -1.0
        v2  = self.conv(v0) + v1
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
