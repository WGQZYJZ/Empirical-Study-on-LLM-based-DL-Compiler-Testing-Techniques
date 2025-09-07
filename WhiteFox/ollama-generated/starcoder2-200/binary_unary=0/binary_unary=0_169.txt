
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return torch.relu(v2)


# Initializing the model
m  = Model()


# Inputs to the model
other  = torch.randn(480, 3, 65, 97) # We add a randomly generated tensor as an argument of the ReLU function. You may choose other tensors or constants that satisfy the requirements.
x1     = torch.randn(28, 3, 84, 69)

