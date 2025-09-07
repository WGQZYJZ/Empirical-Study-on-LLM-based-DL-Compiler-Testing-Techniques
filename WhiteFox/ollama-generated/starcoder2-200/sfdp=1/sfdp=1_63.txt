

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.matmul
 
    def forward(self, query, key, value):
        v1  = self.matmul(query, key)
        v2  = v1 / float(64) # Scale the dot product by an inverse scale factor that is 1/64
        v3  = v2.softmax(-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.875) # Apply dropout to the scaled dot product with a probability of 0.875
        v5  = self.matmul(value, v4) # Compute the dot product between the value tensor and the dropout output
        return v5

m  = Model()

 x1 = torch.randn(2, 64, 32, 32)
x2 = torch.randn(2, 64, 32, 32)
x3 = torch.randn(2, 64, 32, 32)

 