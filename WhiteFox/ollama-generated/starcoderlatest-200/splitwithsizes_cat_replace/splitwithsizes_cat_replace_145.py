
class Model(torch.nn.Module):
    def __init__(self, split_size=1, cat_dim=-1):
        super().__init__()
        self.split = torch.nn.SplitWithSizes([0], [split_size])
        self.cat = torch.nn.Cat((cat_dim,), dim=cat_dim)
 
    def forward(self, x1):
        v = self.split(x1)
        return self.cat(*v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2048, 64, 3, 256, device=DEVICE)
