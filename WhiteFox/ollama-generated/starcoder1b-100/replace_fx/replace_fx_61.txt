
class Model(torch.nn.Module):
    def __init__(self, fallback_random=False):
        super().__init__()
        if torch.cuda.is_available():
            self.linear = nn.Linear(2, 2).cuda()
        else:
            self.linear = nn.Linear(2, 2)

        if fallback_random:
            self.dropout1 = nn.Dropout(0.5)

    def forward(self, x1):
        v1 = self.linear(x1)
        if self.training and random():
            return self.dropout1(v1)
        else:
            return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
