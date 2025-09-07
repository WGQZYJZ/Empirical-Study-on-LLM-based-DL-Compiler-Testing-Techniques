
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(v1.size()[1], -1) # Sink this tensor. The optimization is triggered here.
        v3 = torch.relu(v2)
        return v3


# Initializing the model and generating random input tensors
m  = Model()
x1, x2 = torch.randn(4, 3), torch.randn(4, 5) # Generate 4 tensors with sizes (4, 3) and (4, 5).
