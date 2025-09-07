
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(5, 32, kernel_size=4)
        self.layernorm = torch.nn.LayerNorm(4)
        self.conv1x1 = torch.nn.Conv1d(32, 32, kernel_size=1)

    def forward(self, x):
        x = self.conv1x1(F.gelu(self.layernorm(self.conv1d(x)))))
        return F.gelu(x)


# Initializing the model
m = Model()


