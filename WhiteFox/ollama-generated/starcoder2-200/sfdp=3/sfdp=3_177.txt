
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v1  = torch.matmul(q1, k1.transpose(-2,-1)) 
        v2  = v1 * scale_factor
        v3  = softmax(v2)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4


# Initializing the model