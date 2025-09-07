
class TransformerModel(torch.nn.Module):
    def __init__(self, ninp, nhid, nlayers, dropout=0.5):
        super().__init__()
        from torch.nn import TransformerEncoder, TransformerEncoderLayer
 
        self._model = TransformerEncoder(
            TransformerEncoderLayer(ninp, nhid, dropout=dropout), 1)
 
    def forward(self, src_seq, query, attn_mask=None):
        return self._model(src_seq + query.unsqueeze(-2), attn_mask)[0]
 
ninp = 48
nhid = nlayers = 6 # These should be the same as those in the previous model
dropout = 0.5 # Should not be the same as that in the previous model, since the masks are different. Also, it shouldn't be used by the dropout module from PyTorch.
m2 = TransformerModel(ninp=ninp, nhid=nhid, nlayers=nlayers)
 
# Inputs to the model
src_seq  = torch.randn(160758493, 32035875, 3) # Size 1x160758493x32035875
query   = torch.randn(nlayers * nhid, ninp) # size 1x6*48x3
 
__output__  = m2(src_seq, query).transpose(-2, -1)

