
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs): # Variable length input list
        t0 = torch.cat(inputs, dim=1)
        t1  = t0[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        return t1

# Initializing model with input tensors
m  = Model()
x1, x2  = torch.randn(32, 3), torch.randn(64, 3)
