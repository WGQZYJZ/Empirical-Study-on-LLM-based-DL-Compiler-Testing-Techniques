
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = x1.permute(0, 2, 1).contiguous() # Permute the input tensor
        v4  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)

        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(200, 2, 80).cuda()
__output__  = m(x1)
