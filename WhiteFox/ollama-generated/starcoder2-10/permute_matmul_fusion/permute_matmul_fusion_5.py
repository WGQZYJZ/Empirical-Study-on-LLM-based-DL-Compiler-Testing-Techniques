
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute((0, 3, 4))
        v2 = torch.bmm(v1, x2) # or torch.matmul(v1, x2)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 3, 5120, 768, 768).cuda() # or torch.rand(64, 3, 5120, 768, 768)
x2 = torch.randn(64, 768, 5120).cuda() # or torch.rand(64, 768, 5120)

