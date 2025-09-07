
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3


# Initializing the model and setting `other` as a tensor with the shape `[64]` that is filled with the value 0.5
m = Model()
m.linear.weight.data = torch.ones(32, 64).div_(18)
m.linear.bias.data = torch.zeros(32)
other = torch.tensor([0.5] * 64, requires_grad=True)


# Inputs to the model