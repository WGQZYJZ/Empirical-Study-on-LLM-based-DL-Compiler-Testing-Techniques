
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query = self.conv(x1).view(-1, 8, 64, 64)
        key   = self.conv(x1).view(-1, 8, 64, 64)
        v1    = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(1024 * 16 * 56 * 56)
        attention_weights = F.softmax(v1, dim=-1)
        output = attention_weights.matmul(self.conv(x1).view(-1, 8, 64, 64))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
