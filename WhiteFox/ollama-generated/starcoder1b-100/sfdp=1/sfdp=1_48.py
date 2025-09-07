
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) / 1e-6 # Compute the dot product of the input and itself
        v = torch.nn.functional.dropout(qk.softmax(-2), p=0.8)
        return self.conv(v)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
