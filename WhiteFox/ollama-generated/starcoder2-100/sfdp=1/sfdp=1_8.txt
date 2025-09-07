
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.softmax

    def forward(self, k1, v2):
        v3  = torch.matmul(k1, v2.transpose(-2,-1)) 
        v4  = v3 / scale_factor
        return self.matmul(v4)


# Initializing the model
m  = Model()
# Inputs to the model
k1 = torch.randn(50, 128)
v2 = torch.randn(50, 128, 64, 32)

