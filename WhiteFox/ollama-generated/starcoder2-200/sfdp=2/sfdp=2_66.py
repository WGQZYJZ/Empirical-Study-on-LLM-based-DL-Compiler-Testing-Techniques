
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(4,8) # A query layer
        self.key = torch.nn.Linear(32,16) # A key layer
        self.value  = torch.nn.Linear(750,8) # A value layer
        self.dropout_p  = 0.5 # Dropout probability
        self.inv_scale_factor = 4 * math.sqrt(torch.FloatTensor([1]).cuda())
 
    def forward(self, query):
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = qk.div(inv_scale_factor)
        v3  = scaled_qk.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v5  = dropout_qk.matmul(value)
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(1024, 3*7*7).cuda()
