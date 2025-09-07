
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64, 1)
 
    def forward(self, x1, other=0.5):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2
# Initializing the model
m = Model()


