
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x):
        return self.linear(x) * torch.rand(x.shape[0], 3)


# Initializing the model
m = Model()


