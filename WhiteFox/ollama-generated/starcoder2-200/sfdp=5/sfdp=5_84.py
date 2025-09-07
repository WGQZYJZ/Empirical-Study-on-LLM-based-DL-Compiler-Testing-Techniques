
class Model(torch.nn.Module):
    def __init__(self, hparams):
        super().__init__()
        self.q = torch.nn.Linear(32, 64)
 
    def forward(self, input1):
        v1  = self.q(input1).transpose(-2,-1) / math.sqrt(32) 
        v2  = v1 + attn_mask
        v3  = torch.softmax(v2, dim=-1)
        return v3

