
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v  = F.elu(self.conv1(x))
        v = F.dropout(v, p=dropout_p, training=training)
        v  = self.conv2(v)
        return v


# Initializing the model
m = Model()


