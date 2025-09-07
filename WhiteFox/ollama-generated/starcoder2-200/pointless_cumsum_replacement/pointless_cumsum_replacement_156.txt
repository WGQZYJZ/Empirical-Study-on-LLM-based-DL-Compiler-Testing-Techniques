
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1): 
        v1 = self.conv(x1) 
        v2 = torch.full([v1.shape[0], v1.shape[-2]*v1.shape[-1]], 
                         1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3 = convert_element_type(v2,dtype) 
        v4 = torch.cumsum(v3,1)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn([1,8,64,64])


