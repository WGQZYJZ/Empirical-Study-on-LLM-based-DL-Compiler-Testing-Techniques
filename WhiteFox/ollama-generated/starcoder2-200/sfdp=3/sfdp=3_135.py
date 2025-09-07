
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) 
        scale  = torch.randn([4,3])
        v2 = v1 * scale 
        v3 = v2.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(v3, p=0.5) 
        v6 = dropout_qk.matmul(value) # dot product 
        return v6


# Initializing the model and generating inputs