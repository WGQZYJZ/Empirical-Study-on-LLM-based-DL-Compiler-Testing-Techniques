
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(2,3)
        self.key  = torch.randn(512*4, 600)
        self.attn_mask  = torch.zeros([512*4-3, 512*4]) 
        for i in range(512):
            j = (i+3)%600
            self.attn_mask[:,j] += 1
    
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, self.query)
        v2  = torch.nn.functional.linear(v1, self.key).transpose(-2,-1) / math.sqrt(3) 
        v3  = v2 + self.attn_mask[:, :self.attn_mask.size()[0]]
        v4  = torch.softmax(v3, dim=-1)
        v5  = torch.nn.functional.linear(v4, x1)
        return v5
        

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2*600, 8)


# Output of the model
