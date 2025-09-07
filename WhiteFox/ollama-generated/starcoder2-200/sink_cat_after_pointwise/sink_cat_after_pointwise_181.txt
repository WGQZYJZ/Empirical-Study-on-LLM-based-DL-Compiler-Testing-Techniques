

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 2)

    def forward(self, x1):
       return torch.relu(x1.view(-1).permute([0, 3]))


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.rand(30, 2)

__output__  = m(x1)