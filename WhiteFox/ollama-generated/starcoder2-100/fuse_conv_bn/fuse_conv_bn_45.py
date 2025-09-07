
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv3d(x1) 
        v2 = torch.nn.functional.batch_norm(v1, momentum=0.95)  # BatchNorm should be in eval mode and batch norm tracking stats
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 16, 8, 7)
