
class Model(torch.nn.Module):
    def __init__(self, dim=2048):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(dim, dim // 8, 1, stride=1)
        self.key_conv = torch.nn.Conv2d(dim, dim // 8, 1, stride=1)
        self.value_conv = torch.nn.Conv2d(dim, dim // 8, 1, stride=1)
        self.fc = torch.nn.Linear(dim, 1)
 
    def forward(self, x):
        query_layer  = self.query_conv(x)
        key_layer     = self.key_conv(x)
        value_layer   = self.value_conv(x)
        output = torch.tanh(torch.matmul(query_layer, key_layer) + self.fc) * (1 / 0.7071067811865476)
        return output

# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(32, 3, 64, 64)
