
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
        self.leaky_relu = nn.LeakyReLU()
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2 == 1., v1, v3)
        v5 = self.leaky_relu(v4)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 2048).cuda() # 64 is a batch size
