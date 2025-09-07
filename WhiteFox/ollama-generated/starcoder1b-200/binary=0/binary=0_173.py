

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2, 3)
        self.fc2 = torch.nn.Linear(3, 4)

    def forward(self, x1, *other):
        v1 = self.fc1(x1) + other[0] # Add another tensor to the output of the convolution
        v2 = self.fc2(v1) + other[1] # Add another tensor to the output of the error function
        return v2


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_0  = torch.nn.Linear(3, 4)
        self.sigmoid   = torch.nn.Sigmoid()

    def forward(self, x1, *other):
        v1 = self.linear_0(x1) + other[0]
        v2 = self.sigmoid(v1) + other[1]
        return v2
