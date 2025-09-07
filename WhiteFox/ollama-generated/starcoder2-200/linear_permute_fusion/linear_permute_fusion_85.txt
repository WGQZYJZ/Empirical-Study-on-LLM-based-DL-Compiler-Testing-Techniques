
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear)
        return v3.permute(-2,-3).permute(-4,-5).permute(-6,-7).permute(-8,-9)


# Initializing the model