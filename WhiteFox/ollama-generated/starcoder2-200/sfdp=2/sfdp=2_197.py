
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k1, v1):
        v2 = torch.matmul(q1, k1.transpose(-2,-1)) # Compute the dot product of a query and a key
        v3 = v2 / 0.5 
        v4 = v3.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=0.75 ) # Apply dropout to the softmax output
        