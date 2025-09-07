
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor | float = None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = v1 - other # <--- 'other'
        return v4


# Initializing the model with 'other' being a constant
m_withconstant = Model(torch.randn([3,8,64,64]))

# Inputs to the model
x2  = torch.randn([1, 3, 64, 64])
__output__, v0 = m_withconstant(x2)


# Initializing the model with 'other' being a random tensor
m_withrand = Model() # <-- No argument to 'other'
v0 = torch.randn([1,3,8,8])  # <-- A constant tensor that is not included in 'other'
v2 = m_withrand(x2)

