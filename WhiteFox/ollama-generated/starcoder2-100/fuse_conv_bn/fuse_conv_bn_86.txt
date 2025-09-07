
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.conv3d(x1)  # This line is added by the user
        v2 = torch.nn.functional.batch_norm3d(v1, self.training)

# Initializing the model with a random input tensor and runing it
m = Model()
x1 = torch.rand(4, 50, 64, 64, 64).requires_grad_()
__output__  = m(x1)

