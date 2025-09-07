
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        w_w = (self.conv(x1).unsqueeze(-1) * self.conv(x1).unsqueeze(-2)).sum(-1) / \
             ((torch.abs(x1)) ** 2).mean(-1).sqrt()
        return w_w


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
