
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input_tensor = torch.randn(1, 3, 64, 64)

    def forward(self):
        t1 = torch.cat([self.input_tensor[:, :2], self.input_tensor[:, :, 9:]], dim=1)
        return t1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
