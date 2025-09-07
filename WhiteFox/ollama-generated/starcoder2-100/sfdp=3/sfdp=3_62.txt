
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): # Inputs to the model. x1: shape (256, 384), x2: shape (384, 90) 
        v1 = torch.matmul(x1, x2).div(scale_factor)
        v2 = v1.softmax(dim=-1) # softmax on the dot product of query and key tensors
        v3 = v2.mul(x3) # dropout
        return v3

# Initializing the model
m  = Model()

# Inputs to the model<|end_of_input|>
x1 = torch.randn([256, 90])
x2 = torch.randn([384, 90])
x3 = torch.randn([384, 768])

