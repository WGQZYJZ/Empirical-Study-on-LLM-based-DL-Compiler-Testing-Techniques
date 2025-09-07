
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        l1  = self.conv1(x1)
        l2  = l1 + 3
        l3  = torch.clamp_min(l2, 0)
        l4  = torch.clamp_max(l3, 6)
        l5  = l4 / 6
    return l5


# Initializing the model and assigning a name to each parameter tensor in the model
m1 = Model()
param1 = m1.conv1.weight; param2 = m1.conv1.bias

# Inputs to the model