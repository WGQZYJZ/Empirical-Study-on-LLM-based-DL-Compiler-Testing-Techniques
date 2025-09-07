
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1[0], x2], dim=1) 
        return v1[:, 9223372036854775807:size]
 

# Initializing the model with input tensors. Notice that this time the number of inputs to the model will not be fixed!
m = Model()
x1, x2 = torch.randn(1, 9223372036854775807), torch.randn(1, size)

