
class LinearGate(torch.nn.Module):
    def __init__(self, gate_num):
        super().__init__()
        self.gate_num = gate_num
 
    def forward(self, x1):
        t1  = self.linear_transformation(x1)
        t2  = torch.sigmoid(t1)
        t3  = x1 * t2
        return t3


# Initializing the model
l = LinearGate(gate_num=3)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
