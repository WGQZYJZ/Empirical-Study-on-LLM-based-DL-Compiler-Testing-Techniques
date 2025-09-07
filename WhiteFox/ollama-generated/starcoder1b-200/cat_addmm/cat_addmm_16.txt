
class Model(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear = torch.nn.Linear(num_features, 1)
 
    def forward(self, x1):
        v = self.linear(x1)
        return v


# Initializing the model
m = Model(256)
