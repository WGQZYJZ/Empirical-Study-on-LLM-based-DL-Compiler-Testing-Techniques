
class Model(torch.nn.Module):
    def __init__(self, input_tensor: torch.Tensor):
        super().__init__()
        self.input_tensor = input_tensor
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.cat([x1.contiguous(), x2], dim=0)
        v3 = self.linear(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 2, 2)
