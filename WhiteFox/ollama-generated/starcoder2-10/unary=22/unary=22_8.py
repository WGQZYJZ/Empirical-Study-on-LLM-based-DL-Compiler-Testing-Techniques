
class Model(torch.nn.Module):
    def __init__(self, in_features=1024, out_features=768):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features)

    def forward(self, x):
        v1  = self.linear(x) 
        return torch.tanh(v1)


# Initializing the model