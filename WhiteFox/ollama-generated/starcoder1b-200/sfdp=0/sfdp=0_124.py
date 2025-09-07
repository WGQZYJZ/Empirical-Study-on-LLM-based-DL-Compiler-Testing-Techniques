
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(256 * 8 * 8, 1)
 
    def forward(self, x):
        x = x.view(x.shape[0], -1)
        x = self.fc(x)
        return x


# Initializing the model
m = Model()


