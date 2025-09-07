
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 32, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return relu(v1 - 0.5)


# Initializing the model
m = Model()


