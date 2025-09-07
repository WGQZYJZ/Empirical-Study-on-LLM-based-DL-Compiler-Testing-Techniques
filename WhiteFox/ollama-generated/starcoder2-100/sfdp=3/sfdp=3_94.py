
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.rand(1, ))
        self.dropout  = torch.nn.Dropout(0.5)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = self.dropout(v3)
        __output__  = dropout_qk.matmul(value)
