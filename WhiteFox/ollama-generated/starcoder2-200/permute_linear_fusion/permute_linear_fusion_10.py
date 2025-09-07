
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        t2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return t2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 50, 48).permute(0, 2, 1).cuda()
