
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x1):
        v1 = F.avg_pool2d(x1, kernel_size=8)
        v2 = F.relu(v1)
        return self.linear(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 32, 64, 64)
