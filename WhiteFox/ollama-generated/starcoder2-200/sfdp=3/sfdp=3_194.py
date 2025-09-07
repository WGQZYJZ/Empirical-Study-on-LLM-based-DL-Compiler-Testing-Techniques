
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = 0.7599982631841505
        self.dropout_p  = 0.5
 
    def forward(self, query, key, value):
        vq  = torch.matmul(query, key.transpose(-2, -1))
        vs  = vq.mul(self.scale)
        vsm  = vs.softmax(dim=-1) 
        vdrop_qk  = torch.nn.functional.dropout(vsm, p=self.dropout_p)
        out  = vdrop_qk @ value
        return out


# Initializing the model
m  = Model()


# Inputs to the model
__query__  = torch.randn(2048, 1536)
__key__  = torch.randn(2048, 1536)
value = torch.randn(2048, 768)

 __output__m( __query__, key, value )
