
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64 * 17 * 29, 3)
 
    def forward(self, x1):
        v1 = F.linear(x1, weight=self.fc.weight, bias=self.fc.bias)
        return F.relu(v1)


# Initializing the model
m = Model()

