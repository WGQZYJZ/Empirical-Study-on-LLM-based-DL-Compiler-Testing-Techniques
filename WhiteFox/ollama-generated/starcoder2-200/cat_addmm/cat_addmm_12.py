
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat = torch.rand((4096*32,), 8)

    def forward(self, input):
        v1 = torch.addmm(input[:, : ,:].clone(), self.mat, self.mat)
        v2 = torch.cat([v1], dim=dim)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn((3045,), 8).reshape(79, 16, 8*8)*torch.rand(2, 32, 4096) # Random input tensor


