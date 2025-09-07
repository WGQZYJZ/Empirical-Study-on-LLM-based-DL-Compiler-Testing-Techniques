
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn = torch.nn.Linear(8 * 64 * 64, 8 * 64 * 64)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        output = self.dropout(self.attn(v6).view(-1, 8 * 64, 64, 64))
        return output

# Initializing the model
m = Model()

