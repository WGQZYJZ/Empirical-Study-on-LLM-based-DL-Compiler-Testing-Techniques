
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        w1 = torch.randn(4, 8, 64, 64)
        qk = torch.matmul(v1, w1).mul(scale_factor).softmax(-1)
        v2 = torch.nn.functional.dropout(qk, p=dropout_p)
        return v2

 # Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
