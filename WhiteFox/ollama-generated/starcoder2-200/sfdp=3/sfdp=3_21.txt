
class AttentionModel(torch.nn.Module):
    def __init__(self, embedding_size=768, scale_factor = 1024., dropout_p = 0.5):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p
        self.query = torch.nn.Linear(embedding_size, embedding_size)
        self.key   = torch.nn.Linear(embedding_size, embedding_size)
        self.value  = torch.nn.Linear(embedding_size, embedding_size)
 
    def forward(self, query):
        q1 = self.query(query)
        k1 = self.key(q1)
        v1 = self.value(q1)

        qk = q1 @ k1.transpose(-2, -1).contiguous() / np.sqrt(k1.size(-1))
        
        sqk  = qk * scale_factor
        softmax_qk = torch.nn.functional.softmax(sqk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)

        output = dropout_qk @ v1
        return output

m  = AttentionModel()

query = torch.randn(2048, 768) # Initializing query tensor

# The model is called with the initial query tensor as an input argument
out = m(query)

