class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1  = torch.nn.Linear(784, 50)
        self.layer2  = torch.nn.Linear(50, 30)
        self.layer3  = torch.nn.Linear(30, 10)

    def forward(self, x):

        v1 = self.layer1(x)
        v2 = relu(v1) # Apply ReLU activation function
        v4 = self.layer2(v2)
        v5 = relu(v4) # Apply ReLU activation function
        v6  = self.layer3(v5)

        return v6
