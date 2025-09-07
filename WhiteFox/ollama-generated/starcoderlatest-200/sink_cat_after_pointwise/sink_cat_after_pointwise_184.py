
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1) # concatenate x1 and x2 along dimension 1
        t2 = t1.view(t1.size(0), -1)  # reshape the concatenated tensor to a vector
        t3 = torch.relu(t2)  # apply relu function on reshaped tensor
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 1, 2)
x2 = torch.randn(2, 1, 2)
