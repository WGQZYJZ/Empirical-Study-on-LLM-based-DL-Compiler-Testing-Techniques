
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.linear  = torch.nn.Linear(3, 4)
        self.relu1   = torch.nn.ReLU()

    def forward(self, x):
        v1 = torch.nn.functional.linear(x[0], self.linear.weight) 
        v2 = v1 + self.linear.bias[None]
        v3 = self.relu1(v2)
        return [v3]

m  = Model()

