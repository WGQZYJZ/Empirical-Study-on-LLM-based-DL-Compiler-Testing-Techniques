
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2,-1))
        v2  = v1 * scale_factor
        v4  = v2.softmax(dim=-1)
        v5  = v4.dropout(p=dropout_p) # dropout in the middle
        v6  = value3 .matmul(v5)
        return v6

# Initializing the model
m  = Model()


# Inputs to the model