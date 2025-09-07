
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        scale = 0.25
 
        v1 = torch.matmul(query1, key1.transpose(-2, -1))
        v2 = v1 * scale
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.1)
        v5 = v4.matmul(value1)
        return v5

# Initializing the model
m  = Model()

# Inputs to the model 
query2   = torch.randn(32, 64, 78, 99).to("cuda") # A tensor with shape [N, Lq, H, W] that contains query information for transformer attention mechanisms.
key1     = torch.randn(32, 64, 99, 50)            # A tensor with shape [N, Lk, H, W] that contains key information for transformer attention mechanisms.
value1   = torch.randn(32, 64, 78, 50).to("cuda") # A tensor with shape [N, Lv, H, W] that contains value information for transformer attention mechanisms.
