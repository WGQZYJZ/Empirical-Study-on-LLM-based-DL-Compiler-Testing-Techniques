
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 1) 
        self.key = torch.nn.Linear(3, 1)
        self.value  = torch.nn.Linear(3, 8)
    
    def forward(self, x1):
        v1  = self.query(x1) # Applies a linear transformation to the query input tensor and returns its output
        v2  = self.key(v1).transpose(-2, -1) # Applies another linear transformation on the output of the first linear transformation, transposes the key tensor and then returns its output
        v3  = torch.matmul(x1, v2) 
        return v3

m  = Model()

