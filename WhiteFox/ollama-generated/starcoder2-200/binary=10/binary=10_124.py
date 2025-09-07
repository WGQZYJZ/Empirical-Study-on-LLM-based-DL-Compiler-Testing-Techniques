
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other # add another tensor here
        return v2


# Initializing the model
m = Model()

