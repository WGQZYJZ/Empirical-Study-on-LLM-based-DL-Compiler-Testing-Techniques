
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 64)
 
    def forward(self, x1):
        v1 = F.leaky_relu(F.avg_pool2d(x1, kernel_size=3))
        v2 = self.linear(v1)
        return F.tanh(v2)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 64 * 7 * 7)
