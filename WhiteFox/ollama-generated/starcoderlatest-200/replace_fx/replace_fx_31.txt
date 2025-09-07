
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=0.5)

    def forward(self, x1):
        v1  = self.dropout(x1)
        v2  = torch.rand_like(v1, dtype=torch.float32, device='cuda', requires_grad=True) # The type will be inferred if possible for the current execution path and CUDA available
        return v2


# Initializing the model
m = Model()
x = torch.randn(10, 5, 1, 64)

