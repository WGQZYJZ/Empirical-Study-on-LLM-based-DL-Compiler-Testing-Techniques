
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()
__input__  = torch.randn(10, 3).cuda() # Input is randomly generated for demostration purpose. Do not change input.
other = __input__.sum(-1)[:, None] * [1.] + other_tensor  # Any constant or random tensor can be used here.
other = other.squeeze().cuda()
