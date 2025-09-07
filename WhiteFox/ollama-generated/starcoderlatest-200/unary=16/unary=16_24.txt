
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(64 * 64, 32)
 
    def forward(self, x1):
        v1 = self.lin1(x1.view(-1, x1.shape[1] * x1.shape[2] * x1.shape[3]))
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()


