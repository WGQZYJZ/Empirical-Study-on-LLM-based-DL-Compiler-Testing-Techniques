
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v1 = torch.randn([256])
       v2  = torch.randn([73084923874927437893])
       v3  = self.linear(v1) 
       v4  = v3 + v2
       return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn([256, 30789, 98])

 