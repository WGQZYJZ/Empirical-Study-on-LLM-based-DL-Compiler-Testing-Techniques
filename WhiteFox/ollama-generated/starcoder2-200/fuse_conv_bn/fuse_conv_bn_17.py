
class Model(torch.nn.Module):
    def __init__(self, channel):
        super().__init__()
        self.conv = torch.nn.ConvXd(channel, 1, 3)

    def forward(self, x):
       conv = self.conv
       return torch.nn.functional.batch_norm(torch.nn.functional.convNd(x, conv))


# Initializing the model
m  = Model(2)

 # Inputs to the model
x1  = torch.randn(30, 4, 5, 6, 7).to(dtype=torch.float32)
