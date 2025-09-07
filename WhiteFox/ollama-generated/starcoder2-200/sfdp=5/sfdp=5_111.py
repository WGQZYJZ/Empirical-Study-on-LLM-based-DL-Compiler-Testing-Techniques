class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.k = torch.randn(4, 2)  # Set the key to a random tensor with shape (4, 2)
        self.v = torch.randn(32, 16)  # Set the value to a random tensor with shape (32, 16)
 
    def forward(self): 
        self.k  = torch.dropout(self.k, 0.95, False).transpose(-2, -1)
        v1 = torch.softmax((self.k @ self.v), dim=-1)
        v1  = (torch.dropout(v1 , 0.35))
        self.output   = ((v1 @ self.v), v1)
        return v1,self.output

self._input = torch.randn(4, 8)
