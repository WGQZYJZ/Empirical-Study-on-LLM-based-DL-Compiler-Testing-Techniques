
class Model(torch.nn.Module):
    def __init__(self, min_value=1., max_value=32768.):
        super().__init__()
        self.linear = torch.nn.Linear(50, 4)
        self.relu   = torch.nn.ReLU()
        self.max    = torch.nn.Softmax(dim=-1)
        self.min    = torch.tensor(min_value).view(-1, 1)
        self.max    = torch.tensor(max_value).view(-1, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return self.max - (self.relu(self.linear(x)) * self.max)


# Initializing the model
m  = Model(min_value=0., max_value=1.)

