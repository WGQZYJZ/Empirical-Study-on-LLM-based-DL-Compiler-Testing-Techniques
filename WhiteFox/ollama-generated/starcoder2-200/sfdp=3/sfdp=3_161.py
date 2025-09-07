
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1.transpose(-2, -1)) * scale_factor
        v3  = torch.softmax(v2)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = v4 @ v1
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
q1   = torch.randn(batchsize, length1, embeddingdim1)
k1   = torch.randn(batchsize, embeddingdim2, length2)
v1  = torch.randn(batchsize, length3, embeddingdim4)


__output__  = m(q1, k1, v1)

