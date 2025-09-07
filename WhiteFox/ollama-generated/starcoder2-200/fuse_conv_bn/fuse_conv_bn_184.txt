
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v3  = self.linear(v1) 
        return v3
# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 4)


# Expected outputs from the model
__output__   = m(x1)

# Desired output shape of tensor
print("Expected 0 4 output")
__expected_shape__  = (0, 4)



