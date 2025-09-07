
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(48, 96)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = v1 + x2 # other
        return v2

# Initializing the model
m  = Model()

# Inputs to the model: Two tensors that are different from each other (i.e., they have a different size or different types of elements, but they represent the same mathematical concept)
x1 = torch.randn(48, 96).requires_grad_(True)
x2 = torch.randn(50, 100).requires_grad_(True)

# Forward pass: Applying the model to input tensors
