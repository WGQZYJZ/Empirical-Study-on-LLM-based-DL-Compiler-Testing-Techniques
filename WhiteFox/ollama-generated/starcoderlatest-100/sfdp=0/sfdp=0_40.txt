
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 1024, 512)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1.view(-1, 64 * 1024))
        v2 = v1.softmax(dim=-1).matmul(x2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 64, 1024)
