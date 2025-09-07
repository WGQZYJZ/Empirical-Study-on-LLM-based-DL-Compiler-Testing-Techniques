
class Model(torch.nn.Module):
    def __init__(self, input1_shape=[50], input2_shape=[784]):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1 for _ in range(len(input1_shape))], dim=0) 
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
v1 = torch.randn(*input1_shape)
v3 = torch.randn(*input2_shape)
__output__  = m(v1, v3)