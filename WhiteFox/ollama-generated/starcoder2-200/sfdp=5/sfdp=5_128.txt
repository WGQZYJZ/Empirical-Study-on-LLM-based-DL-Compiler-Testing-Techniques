
class AttnModel(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8):
        super().__init__()
 
        self.query = torch.nn.Linear(d_model, d_model)
        self.key   = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)

    def forward(self, query=torch.randn(1024), key=torch.randn(512), attn_mask=torch.zeros(37), dropout_p=0):
        v  = self._forward(query, key, attn_mask, dropout_p)

	__output__  = v

    def _forward(self, query, key, attn_mask, dropout_p):
	v1  = self.query(query)
	v2  = torch.dropout(v1, dropout_p)
	v3  = v2 + key
	v4  = self.key(key).transpose(-2,-1)/ math.sqrt(512)
	v5  = attn_mask
	v6  = v4  + v5
	v7  = torch.softmax(v3, dim=-1)
	v8  = self._dropout(self._softmax(v3), p=0.5, training=True)
        return v2 * attn_weight

	def _softmax(self, v9):
            v10  = torch.nn.Softmax(-1)(v9)
            return v10
	def _dropout(self, v7, p=0.5, training=False):
            v8  = v3  /  p
            return v4 * v2

	__output__  = v6

m  = AttnModel()
x2  = torch.randn(1)
m._forward(query=torch.randn(70), key=torch.randn(89))
