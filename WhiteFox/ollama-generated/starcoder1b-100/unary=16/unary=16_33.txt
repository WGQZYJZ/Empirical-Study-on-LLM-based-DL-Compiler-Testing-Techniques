
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 3)
 
    def forward(self, x1):
        v1 = F.relu(F.linear(x1, weight=self.weight))
        return v1


# Initializing the model
m = Model()


