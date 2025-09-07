
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2.transpose(-2, -1))
        v2  = v1 / math.sqrt(64)
        v3  = nn.functional.softmax(v2) # Apply softmax to the scaled dot product
        v4  = dropout(v3, p=0.5) # Apply dropout to the softmax output
        return v4
