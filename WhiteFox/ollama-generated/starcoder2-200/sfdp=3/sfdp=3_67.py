
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(3, 4)
        self.query = torch.nn.Linear(5, 20)
 
    def forward(self, x1, x2):
        vq = self.query(x2)
        vk = self.key(x1).transpose(-2, -1)
        scale_factor = vq.size(-1)**-0.5
        
        vqk = torch.matmul(vq, vk) / 368 # Scale the dot product by a factor (divided by 368)
        vs = vqk.mul(scale_factor)
 
        vsm = vs.softmax(dim=-2)
        vdm = torch.nn.functional.dropout(vsm, p=0.1)
        res = vdm * x2
        
        return res


# Initializing the model 
m = Model()

# Inputs to the model
x1  = torch.randn(489,3) # key tensor of shape [n_heads, length, head_dim]
x2 = torch.randn(501 , 5) # query tensor of shape [n_heads, query_length, query_head_dim]

 __output__= m(x1, x2).shape

