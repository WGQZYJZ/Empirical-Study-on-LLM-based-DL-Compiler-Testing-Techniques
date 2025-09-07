
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    @torch.jit._export()
    def forward(self, x1, bn_params):
        conv = torch.nn.functional.conv2d(x1, bn_params["weight"], bn_params["bias"])
        return torch.nn.functional.relu(bn(conv))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
