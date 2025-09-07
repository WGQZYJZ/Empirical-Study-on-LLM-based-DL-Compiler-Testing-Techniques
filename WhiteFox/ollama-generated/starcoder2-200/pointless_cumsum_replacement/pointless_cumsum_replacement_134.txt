
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cumsum  = torch.nn.CumSum()
 
    def forward(self, x):
        v1  = x 
        v2  = torch.full([v1.size()[0], 384, 769, 512], 1, dtype=torch.int64)
        v3  = convert_element_type(v2,  torch.float32)
        v4  = self.cumsum(v3) # Convert v1 to float and then compute the cumulative sum of its elements along dimension 0. 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn([5, 769, 28])
__output__  = m(x1)

