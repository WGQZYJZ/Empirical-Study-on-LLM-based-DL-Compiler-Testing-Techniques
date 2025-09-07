
class Model(torch.nn.Module):
    def __init__(self, n, k):
        super().__init__()

        self.relu = torch.nn.ReLU()

        # initialize linear layer
        self.linear = torch.nn.Linear(n, 1)

    def forward(self, x1):
        v2 = torch.cat((x1, x1), dim=0).view(-1, 1) 
        v3 = self.relu(v2) # line 8
        return v3


# Initializing the model
m  = Model()

# Input to the model