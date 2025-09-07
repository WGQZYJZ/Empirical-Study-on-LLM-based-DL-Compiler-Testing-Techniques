
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 - other_tensor
        return v2

# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(640, 3).t() # A 3 × 640 tensor.
