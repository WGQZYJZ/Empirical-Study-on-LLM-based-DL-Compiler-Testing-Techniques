
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model and passing in another tensor as a keyword argument to the linear transformation (t2 in the specification). The `other` tensor is passed as a keyword argument here to avoid code duplication with the other model example.
m = Model(x1[0, :, 50:87].view(-1, 3))


# Input to the model
x2 = torch.randn(4, 3, 64, 64)
