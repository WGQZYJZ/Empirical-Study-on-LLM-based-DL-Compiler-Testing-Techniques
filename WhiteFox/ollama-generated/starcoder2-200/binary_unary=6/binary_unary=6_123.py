
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,8)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 - other_tensor
        v4  = torch.relu(v2)

        return v4

# Initializing the model
m = Model()
other_tensor  = torch.randn(8,32,)


# Inputs to the model
input1 = torch.randn(5000, 64, 32 )
output1 = m(input1)


