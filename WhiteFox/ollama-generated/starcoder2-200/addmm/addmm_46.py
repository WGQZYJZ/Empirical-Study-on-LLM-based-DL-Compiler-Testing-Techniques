
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = torch.randn(4, 9) # The size of the first tensor is (4, 9).
        v1 = torch.mm(v0, v0) # Perform matrix multiplication on two input tensors.
        return v1


# Initializing the model
m = Model()

# Inputs to the model