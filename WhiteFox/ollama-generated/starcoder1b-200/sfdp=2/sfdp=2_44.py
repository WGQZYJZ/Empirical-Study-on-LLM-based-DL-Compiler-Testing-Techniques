
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v2 = v2 * 0.5 + v1
        v3 = torch.softmax(v2, dim=-1)
        return torch.nn.functional.dropout(v3, p=dropout_p)


# Initializing the model
m = Model()


