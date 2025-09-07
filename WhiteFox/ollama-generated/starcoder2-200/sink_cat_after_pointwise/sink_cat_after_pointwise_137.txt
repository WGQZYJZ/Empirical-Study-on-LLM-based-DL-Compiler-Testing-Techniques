
class Model(torch.nn.Module):
    def __init__(self, channel1=20):
        super().__init__()
        self.linear = torch.nn.Linear(channel1+5, 10)

    def forward(self, x):
        t1 = torch.cat([x[:, :channel1], x[:, channel1:]])
        v3  = torch.relu(t1).view(-1, channel1 + 5)
        return self.linear(v3)

# Initializing the model
m = Model()

