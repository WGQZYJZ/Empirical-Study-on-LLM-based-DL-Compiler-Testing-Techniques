
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 2)
        self.layer1 = torch.nn.TransformerEncoderLayer()
 
    def forward(self, x):
        v_out  = torch.nn.functional.adaptive_avg_pool2d(x, (30,30))
        o1  = self.linear1(v_out)
        o2  = self.layer1(o1).mean(-2)
        return o2

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(4, 8, 30, 30)
__output__  = m(x)

