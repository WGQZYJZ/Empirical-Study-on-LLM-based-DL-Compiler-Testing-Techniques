
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.size()[0], -1))
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32 * 32 * 3, device=device) # x1 is in a batch of 64 samples with shape (64, 32 * 32 * 3) where - 32*32*3 refers to the number of pixels per image
