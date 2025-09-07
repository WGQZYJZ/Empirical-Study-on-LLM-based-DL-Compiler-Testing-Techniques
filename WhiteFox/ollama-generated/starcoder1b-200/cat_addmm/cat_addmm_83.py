
class Model(torch.nn.Module):
    def __init__(self, n_input):
        super().__init__()
        self.fc = torch.nn.Linear(n_input, 3)
 
    def forward(self, x1):
        v2 = self.fc(x1)
        return torch.addmm(v2, v2, v2)


# Initializing the model
m = Model(4)


