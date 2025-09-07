
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(...)  # Permute the input tensor A
        v2 = torch.bmm(...)  # or torch.matmul(...), depending on situation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 5)
