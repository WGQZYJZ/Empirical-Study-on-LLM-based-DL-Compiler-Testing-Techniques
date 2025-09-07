
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], 0) 
        v2 = v1.view(-1, self.dim, self.dim) # Sink the cat after pointwise
        v3 = torch.nn.functional.tanh(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model 
x1 = torch.randn(20, 5, 784) # input tensors have the same shape
