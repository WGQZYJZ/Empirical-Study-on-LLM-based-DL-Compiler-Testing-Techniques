
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        q = self.q_conv(x)
        k = self.k_conv(x)
        v = torch.zeros_like(q)
        softmax_qk = (q * k).softmax(dim=-1)
        output = torch.matmul(softmax_qk, v)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
