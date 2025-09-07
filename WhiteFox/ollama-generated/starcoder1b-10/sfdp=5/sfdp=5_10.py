
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn_weights = None
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.attn_weights is None:
            self.attn_weights = torch.softmax(v1 @ x1.transpose(-2, -1), dim=-1)
        output  = self.attn_weights @ v1
        return output


# Initializing the model
m = Model()


