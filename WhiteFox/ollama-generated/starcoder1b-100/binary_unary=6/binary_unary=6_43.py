
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 512, bias=True)
 
    def forward(self, x):
        return F.relu(self.linear(x)) - 0.5


# Initializing the model
m = Model()


