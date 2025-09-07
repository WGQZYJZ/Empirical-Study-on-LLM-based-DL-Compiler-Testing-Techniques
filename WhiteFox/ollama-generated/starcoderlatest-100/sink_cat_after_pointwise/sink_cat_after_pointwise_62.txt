
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=1)
        v1 = t1.view(-1) # Reshape tensor to a vector, this operation is pointless in practice, but serves as a demonstration of `sink_cat_after_pointwise` optimization
        return self.relu(v1)

    def relu(self, x):
        return torch.nn.functional.relu(x)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(100, 32)
x2 = torch.randn(100, 64)
x3 = torch.randn(100, 96)
