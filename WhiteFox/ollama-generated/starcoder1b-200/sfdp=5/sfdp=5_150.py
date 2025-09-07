
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        kx = self.conv(x1) @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        v = torch.softmax((kx + attention_mask).softmax(-1), dim=-1)
        o = v @ value # compute the dot product of the dropout output and the value
        return o


# Initializing the model
m  = Model()


