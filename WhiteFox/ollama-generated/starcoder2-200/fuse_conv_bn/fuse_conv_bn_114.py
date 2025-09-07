
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(3, 100, 5)

    def forward(self, x1):
        conv1  = self.conv(x1)
        return conv1

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor  = torch.randn(200, 30, 3, 50, 64)

 