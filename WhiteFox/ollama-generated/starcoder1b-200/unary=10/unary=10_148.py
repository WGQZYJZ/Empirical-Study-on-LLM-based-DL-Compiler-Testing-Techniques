
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)

    def forward(self, x):
        return self.linear1(x) + 3

    def backward(self, dout):
        dx = dout * self.linear1.bias
        return dx


# Initializing the model
m = Model()

