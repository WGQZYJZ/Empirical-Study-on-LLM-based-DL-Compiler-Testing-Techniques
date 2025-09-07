
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
         v1  = torch.mm(x1, x2)
         v2  = torch.mm(x3, x4)
         v3  = v1 + v2
         return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(50, 96)
x2  = torch.randn(50, 96)
x3  = torch.randn(48, 72)
x4  = torch.randn(48, 72)

 # Running the model for forward pass with the given inputs to the model as arguments. The model should produce a new result based on the provided arguments. The new result is added to the output of the model and sent out as the output of the model.
