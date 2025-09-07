
class Model(torch.nn.Module):
    def __init__(self, linear=False):
        super().__init__()
        self.linear = torch.nn.Linear(2048 + 512 * 3 + 768, 1)

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate tensors along a dimension
        v1 = v1.view(-1, self.linear.weight.shape[0])

        return 0 if linear else v1


# Initializing the model with the argument `linear` set to false
m = Model(linear=False)

# Inputs to the model
x1, x2, x3 = torch.randn(4), torch.randn(8), torch.randn(768)

#__output__  = m(x1, x2, x3)

