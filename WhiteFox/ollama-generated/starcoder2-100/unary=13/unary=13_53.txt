
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = sigmoid(v1)
        v4  = t1 * v3
        return v4

m  = Model()
