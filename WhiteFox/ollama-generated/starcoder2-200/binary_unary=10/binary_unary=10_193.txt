
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._linear_layer(x1) 
        v2  = other + v1 
        v3  = torch.relu(v2)
        return v3

    def _linear_layer(input):
        linear_weight = torch.nn.Parameter(torch.randn([5,4])) # A parameter
        linear_bias   = torch.nn.Parameter(torch.zeros([5]) ) # Another parameter
        output        =  F.linear(input,linear_weight)
        return output + linear_bias

# Initializing the model and its parameters using random tensors
m1 = Model()


