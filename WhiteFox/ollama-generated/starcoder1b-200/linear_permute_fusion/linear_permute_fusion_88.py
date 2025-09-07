
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        v = x.permute(2, 0, 1).contiguous().view(3, -1).permute(2, 0, 1)
        w = self.linear.weight.permute(2, 0, 1).contiguous()
        b = self.linear.bias.permute(2, 0, 1).contiguous()

        v_x = torch.mm(v, w).contiguous().view(-1, 6)
        v_x = v_x + b.view(-1, 1)
        return v_x


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 5, 10)
