
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784,10)

    def forward(self, x): 
        v1  = self.linear(x)
        v2  = v1 - other 
        return v2

# Initializing the model with a fixed `other` tensor to test that it still works for multiple calls of `forward`. We do not initialize the model to `m` to make sure that there is not a cached model in the global namespace.

other  = torch.randn(3,1) * 0.2
print(f"other: {other}")

 # Inputs to the model 

x1 = torch.randn(784,10).float()
__output__m = m(x1)
__output__n = n(x1)

