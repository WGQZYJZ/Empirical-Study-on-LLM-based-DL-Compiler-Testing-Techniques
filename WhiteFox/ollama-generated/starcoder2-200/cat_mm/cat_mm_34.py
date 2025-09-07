
class Model(torch.nn.Module):
    def __init__(self, num_layers=4):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        
        self.layers = torch.nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(torch.nn.Linear(7*7*8, 4))
 
    def forward(self, x):
 
        v1  = conv(x)

        t0  = []
        for idx in range(len(v1)):
           t0 += [idx]
    
        # print(t0, t0[0], len(t0), len(layers), 3, len(conv))
        
        v2  = torch.cat([v1[i] for i in t0], dim=1)
        v3  = self.layers[0](v2)

        return v3


# Initializing the model
m  = Model()
m_new  = Model(num_layers=5)
 
# Inputs to the model
x  = torch.randn(4, 8)
__output__  = m(x)
 
 
 
