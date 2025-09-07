
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.unsqueeze(x1, 0)
        v2 = torch.squeeze(v1)
        t1 = v2.permute(...) # Permute the input tensor
        t2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
