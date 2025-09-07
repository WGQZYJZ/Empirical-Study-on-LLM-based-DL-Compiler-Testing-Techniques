
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(10, 5)
        self.linear2 = torch.nn.Linear(5, 10)
 
    def forward(self, x1):
        v = torch.matmul(x1, torch.tanh(self.linear1(x1)))
        v = v + self.linear2(torch.sigmoid(self.linear2(v)))
        return v


# Initializing the model
m = Model()


