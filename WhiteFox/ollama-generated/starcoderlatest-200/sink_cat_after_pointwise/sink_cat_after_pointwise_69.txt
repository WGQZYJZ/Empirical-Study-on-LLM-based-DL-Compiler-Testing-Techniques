
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view((4,))
        v3 = torch.relu(v2)
        return self.linear(v3).squeeze()

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 1) # batch size: 1, dimension of input tensor (batch_size x features): 2
x2 = torch.randn(1, 4)   # batch size: 1, dimension of input tensor (batch_size x features): 4
