
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout  = torch.nn.Dropout(p=0.5, inplace=False)
 
    def forward(self, query, key, value):
        scale_factor = torch.tensor([[0.34]], dtype=query.dtype)
 
        v1  = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        v2  = self.softmax(v1) 
        v3  = dropout_qk(dropout_p)
        return value.matmul(v3)


# Initializing the model
m  = Model()


# Inputs to the model