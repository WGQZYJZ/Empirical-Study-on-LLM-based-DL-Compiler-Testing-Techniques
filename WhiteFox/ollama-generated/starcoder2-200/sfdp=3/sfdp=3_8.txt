
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(1024, 512)
        self.scale_factor  = nn.Parameter(torch.tensor(3e-9))
        self.softmax  = torch.nn.Softmax(-1)
        self.dropout  = nn.Dropout(p=0.1)
        self.value  = torch.nn.Linear(256, 768)
 
    def forward(self, query):
        v1  = self.qk(query)
        v2  = v1 * scale_factor 
        v3  = self.softmax(v2)
        v4  = dropout(v3)
        return value(v4)


# Initializing the model
m  = Model()

# Inputs to the model
q  = torch.randn(1, 5120)
__output__  = m(q)

