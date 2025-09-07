
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        t1 = torch.mm(v1, x2) # Concatenate along dimension 0
        return t1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(4, 3, 64, 64)
output_tensor = m(input_tensor, input_tensor[:, :, 0:8, 0:8])

