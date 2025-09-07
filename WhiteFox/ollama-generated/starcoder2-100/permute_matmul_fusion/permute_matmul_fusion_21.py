
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1  = x1.permute(0, 2, 1) # Permute the tensor A
        v3  = torch.bmm(v1, x2)   # Use the tensor A as main input to a bmm function
                                # In the original code, the input B is used instead of A.
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 2)
y1  = torch.randn(10, 3)

