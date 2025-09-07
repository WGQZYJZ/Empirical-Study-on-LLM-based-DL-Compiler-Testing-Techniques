
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.v1  = torch.full([4, 3], 5)
        self.v2  = self.v1 + 1
 
    def forward(self, x):
        return convert_element_type(cumsum(convert_element_type(self.v2, dtype), 1), 64)


# Initializing the model
m  = Model() 

# Inputs to the model
x = torch.randn([3] * m.v2.shape[0])
__output__  = m(x)

