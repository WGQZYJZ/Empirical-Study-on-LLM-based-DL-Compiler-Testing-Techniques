
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(data=torch.tensor([0]), requires_grad=True)
        self.dropout  = torch.nn.Dropout(p=1.)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1 * scale
        v3  = torch.softmax(v2, dim=-1)
        v4  = self.dropout(v3)
        v5  = v4.matmul(value)


# Initializing the model
m = Model()
scale = 0.76988 # Initialized with 0.76988 and randomly generated in this task.
m.scale = torch.nn.Parameter(data=torch.tensor([scale]), requires_grad=True)


# Inputs to the model
query  = torch.randn((1, 512, 16), dtype=torch.float32)
key    = torch.randn((1, 48, 512))
value  = torch.randn((1, 512, 17),dtype=torch.float32)

 