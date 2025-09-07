
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, other=None):
        if other is None:
            t3 = torch.nn.functional.relu(t2)
        else:
            t3 = torch.nn.functional.relu(other + t2)
        return t3


# Initializing the model
m = Model()

x1 = torch.randn(1, 1024)
