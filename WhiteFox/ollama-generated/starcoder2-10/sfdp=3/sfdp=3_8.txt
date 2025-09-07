
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = 0.3 
        self.dropout_p= 0.25
        self.weight1, self.bias1, self.weight2 = torch.rand(48 * 69),torch.rand(48), torch.rand((3, 48))
 
    def forward(self, query, key):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1.mul(scale_factor) # scale_factor
        v3  = scaled_qk.softmax(dim=-1) 
        v4  = v3 .dropout(p=dropout_p)  
        v5  = v4.matmul(value)
        return v6

# Initializing the model
m  = Model()
 
 
