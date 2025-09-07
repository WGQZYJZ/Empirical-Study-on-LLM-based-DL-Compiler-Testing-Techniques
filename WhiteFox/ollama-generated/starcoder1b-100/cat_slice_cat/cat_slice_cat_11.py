
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # ... initialize the output tensors here...

# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
