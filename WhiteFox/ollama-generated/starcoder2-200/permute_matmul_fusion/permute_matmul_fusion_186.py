
class Model(torch.nn.Module):
    def __init__(self, A, B):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) 
        v3  = input_tensor_B.permute(...) # Permute the input tensor B in this line
        v4  = torch.bmm(v1, v3)           # or v4  = torch.matmul(v1, v3)
        return self.linear(v2) + v4


# Initializing model with inputs x1 and x2 of different shapes 
x1 = torch.randn((256), 8).permute((0, 2, 1)) # shape (256, 8, 8)
x2 = torch.randn(4, 8).permute((1, 0)).repeat_interleave(256) # shape (32, 2)
m = Model(x1, x2)

# Inputs to the model with inputs x1 and x2 of different shapes  
x1  = torch.randn(4, 8).permute((0, 2)).repeat_interleave(256) # shape (256, 8, 3)
__output__  = m(x1, x2)

