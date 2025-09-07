
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1))
        vs = torch.div(vq, math.pow(math.sqrt(math.pi), math.floor(2 * k_size / 2)))
        self.softmax_qk = vs.softmax(dim=-1)
        self.dropout_qk = torch.nn.functional.dropout(self.softmax_qk, p=dropout_p)
        return self.dropout_qk.matmul(x3)

 # Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
