
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(32, 16)
        self.k = torch.nn.Linear(64, 32)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(32 * (key.shape[-1]))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = torch.matmul(dropout_qk, value)
        return output
 
# Initializing the model and generating inputs for the model.
m  = AttentionModel()
q  = torch.randn(1, 32, 8, 16)
k  = torch.randn(1, 64, 32, 8)
v  = torch.randn(1, 64, 32, 8)
