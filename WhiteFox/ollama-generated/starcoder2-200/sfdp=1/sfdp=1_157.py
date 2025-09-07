
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v  = torch.matmul(query1, key2.transpose(-2, -1)) 
        v1 = v / inv_scale_factor
        v2 = v1.softmax(dim=-1)
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        v4 = v3.matmul(value3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
query1 = torch.randn([8, 600], dtype=torch.float)
key2  = torch.randn([8, 795, 600], dtype=torch.float)
value3 = torch.randn([8, 795, 48])

 __output__  = m(query1, key2, value3)

