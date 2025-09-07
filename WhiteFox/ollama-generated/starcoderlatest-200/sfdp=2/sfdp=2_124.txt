
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(1024, 512)
        self.key   = torch.nn.Linear(1024, 512)
 
    def forward(self, q, k, v):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
 
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk  = F.dropout(softmax_qk, p=0.1)
 
        output    = torch.matmul(dropout_qk, v)
        return output


# Initializing the model
m = Model()
 
