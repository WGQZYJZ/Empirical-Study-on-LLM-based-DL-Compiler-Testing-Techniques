
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight).permute(0, 2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
__output__  = m(x1)

# Expected output
[[-0.8997 -0.3956]

 [-0.0624  1.108 ]
 
 [ 1.134   0.2841]
 
 [-1.4898 -0.694 ]]
