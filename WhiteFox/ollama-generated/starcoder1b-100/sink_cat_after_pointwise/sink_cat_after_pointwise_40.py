
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.view  = torch.nn.View((4, -1))

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1)
        t2 = self.view(t1)
        return self.relu(t2)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 16, 4, dtype=torch.float32, device='cuda')
