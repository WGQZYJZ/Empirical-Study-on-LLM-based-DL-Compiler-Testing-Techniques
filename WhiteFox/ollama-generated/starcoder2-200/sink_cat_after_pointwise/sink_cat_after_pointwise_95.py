
class Model(torch.nn.Module):
    def __init__(self, ksize: int = 3):
        super().__init__()

    def forward(self, x1, y1):
        v0 = torch.cat([x1, x2], dim=...)

        v0 = v0.permute(0, 4, 1, 2) # Sink cat after pointwise
        return v0

# Initializing the model
m = Model()


# Inputs to the model<|end_of_input|>
x1 = torch.randn(5, 32, 7, 7)
y1 = torch.randn(4, 32, 3, 3)

