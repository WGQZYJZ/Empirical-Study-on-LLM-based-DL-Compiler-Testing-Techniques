
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).mul(v1 * 0.7071067811865476).mul(torch.erf(v1)).add(1)
        v3 = ((v1 * 0.5) * (v1 * 0.7071067811865476)).softmax(dim=-1) * (x1 * x1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4


# Initializing the model
m = Model()


