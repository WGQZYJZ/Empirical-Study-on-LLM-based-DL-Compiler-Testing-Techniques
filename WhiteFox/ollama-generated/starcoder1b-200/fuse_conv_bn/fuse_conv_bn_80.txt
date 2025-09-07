
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        output  = self.linear(x1)
        return output


# Inputs to the model
input_tensor = torch.randn(1, 2, 3, 4)
