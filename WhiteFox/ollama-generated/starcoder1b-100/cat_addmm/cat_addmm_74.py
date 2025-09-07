
class Model(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.fc = torch.nn.Linear(n_features, 20)
 
    def forward(self, x1):
        v1 = x1.contiguous().view(-1, 5)
        v2 = self.fc(v1)
        return v2


# Initializing the model
m = Model(20)


