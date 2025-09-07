
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(data=torch.randn(2048, 512))
        self.key  = torch.nn.Parameter(data=torch.randn(64, 32768))
        self.value  = torch.nn.Parameter(data=torch.randn(64, 32768))
        self.scale_factor  = 10
    def forward(self):
        v1  = torch.matmul(self.query, self.key.transpose(-2, -1)) 
        v2  = v1.div(float(self.scale_factor)) 
        v3  = v2.softmax(dim=-1) 
        v4  = dropout(v3)
        return v4.matmul(value)

# Initializing the model
m  = Model()

 # Inputs to the model: 
 torch.randn(1, 512), 
 torch.randn(64, 32768)
 