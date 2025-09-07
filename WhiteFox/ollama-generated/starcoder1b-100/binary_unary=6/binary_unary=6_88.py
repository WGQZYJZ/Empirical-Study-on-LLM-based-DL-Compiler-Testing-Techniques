
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 3 * 7 * 7, 256)
 
    def forward(self, x1):
        v1 = torch.randn(x1.size(0), 64, 3, 7, 7).view(-1, 64 * 3 * 7 * 7)
        return self.linear(v1)


# Initializing the model
m = Model()


