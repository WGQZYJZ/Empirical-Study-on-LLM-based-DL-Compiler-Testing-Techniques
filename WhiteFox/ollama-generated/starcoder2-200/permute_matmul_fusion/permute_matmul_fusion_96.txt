
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # Forward is a keyword, so rename it.
        v1 = torch.bmm(x1.permute(0, 2, 1), y2)

# Initializing the model
m  = Model()


# Inputs to the model
# Assume that x1 and y1 are tensors whose sizes conform to the first scenario described above.
x1 = torch.randn(1, 2, 4)
y1 = torch.randn(3, 4, 5)
