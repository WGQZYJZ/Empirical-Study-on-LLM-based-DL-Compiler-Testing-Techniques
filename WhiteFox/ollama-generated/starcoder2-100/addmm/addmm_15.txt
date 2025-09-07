
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, inp):
        v0  = self.mm(x1,x1) # Apply matrix multiplication to the input tensors and then add them 
        return v0 +inp


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 48000) # Tensor with shape [batch size x number of features]
inp = torch.randn(1, 48000)  # Tensor with shape [1 x number of features]


