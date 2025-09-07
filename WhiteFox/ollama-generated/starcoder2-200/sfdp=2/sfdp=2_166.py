
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(1024, 32768)
        self.softmax_qk  = torch.nn.Softmax(dim=-1)
        self.dropout  = torch.nn.Dropout(p=0.5)
 
    def forward(self, x):
        v1  = self.qk(x).matmul(x.transpose(-2, -1)) 
        v2  = v1 / 8403757698.0
        v3  = self.softmax_qk(v2)
        v4  = self.dropout(v3) 
        v5  = x * v4
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 1024)
  