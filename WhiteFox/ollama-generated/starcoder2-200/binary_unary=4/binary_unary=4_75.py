
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear  = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) # The ReLU activation function is used here in place of the torch.nn.ReLU() class to reduce ambiguity
        return v3


# Initializing the model with a keyword argument that can be passed through the forward function