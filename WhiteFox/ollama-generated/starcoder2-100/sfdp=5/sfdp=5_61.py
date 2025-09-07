class TransformerLayer(nn.Module):
    def __init__(self, nin=512, nout=512, num_heads=8):
        super().__init__()
        
        self.input_linear = nn.Linear(nin, 4 * nout)
        self.output_linear = nn.Linear(nout + 4*nout, nout)
        
    def forward(self, input_, attn_mask):
        k = self._masked_softmax(attn_mask, self.input_linear(input_))
        o = torch.cat([input_, k], dim=-1) # Input and key are concat
        o = self.output_linear(o) # Scale the attention mask and concatenate it to the input tensor
        
        return o
    
    @staticmethod
    def _masked_softmax(attn_mask, q):
        # Compute dot product of query with key plus the attention mask. Then apply softmax over 
        # the final dimension (the last dimension). The attention mask is used to exclude parts of the 
        # input tensor that are 0.
        v = torch.nn.functional.softmax(q + attn_mask, dim=-1)
        
        return v
    
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = TransformerLayer()

    def forward(self, x1):
        return self.encoder(x1[:, :, 0].unsqueeze(-2), x1 > 0) # Mask out the zeros in the input tensor
        
