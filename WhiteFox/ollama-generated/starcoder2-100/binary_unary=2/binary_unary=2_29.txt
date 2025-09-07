
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v4  = relu(v2)
 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


# Initializing the model with custom module
m_custom_module = torch.nn.Conv2d(5, 9, 1, bias=False)
v0 = torch.rand((3,5), dtype=torch.float32).to(torch.device('cuda')) # 5-channel input tensor for Conv2d

class Model_CustomModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = m_custom_module
 
    def forward(self, x1): 
        return v0


# Initializing the model with custom module
m_custom  = Model_CustomModule() 


# Inputs to the model
x2 = torch.randn((5,), dtype=torch.float32).to(torch.device('cuda')) # 4-channel tensor for Custom Module


# Initializing the model with non-sequential submodule
m_submodule = m_custom.conv
v0a  = v0 - other + 5
 

# Inputs to the model from custom module
x1 = torch.randn(1, 3, 64, 64)

