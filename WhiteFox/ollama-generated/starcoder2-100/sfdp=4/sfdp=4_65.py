
class AttnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 4)
        self.key    = torch.nn.Linear(5, 8) 
        self.value  = torch.nn.Linear(7, 12)
 
    def forward(self, x):
        qk_mat = (
            self.query(x).transpose(-2, -1)) @ 
            self.key(x).transpose(-2, -1)
        qk_mat +=  AttentionMask()
        attn_weight = torch.softmax(qk_mat / 
                math.sqrt(qk_mat.size(-1)), dim=-1)
 
        output = (attn_weight @ 
                   self.value(x))
 
        return output

# Initializing the model
m = AttnModel()


# Inputs to the model
__x__  = torch.randn(2, 3) 


