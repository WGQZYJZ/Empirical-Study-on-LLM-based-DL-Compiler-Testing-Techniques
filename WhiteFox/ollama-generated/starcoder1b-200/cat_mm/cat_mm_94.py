
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, kernel_size=1, stride=1)

    def forward(self, x1, x2):
        output = torch.mm(x1, x2)
        concat = [output]
        for i in range(len(concat)):
            concat[i] = self.conv(output) + concat[i]
# Initializing the model
m = Model()


