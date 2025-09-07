
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 196)
        self._other = torch.tensor([8754], dtype=int).cuda()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self._other
        v3 = F.relu(v2)  # Apply ReLU activation function to the result
        return v3


# Initializing model
m = Model()


# Inputs to the model
x1 = torch.randn(7, 40).cuda()
