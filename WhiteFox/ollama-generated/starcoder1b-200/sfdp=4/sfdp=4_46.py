
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 3)
 
    def forward(self, x1):
        output = self.linear(x1).view(-1, 768)
        return output


# Inputs to the model
q1 = torch.randn(1024, 3, 512, 512) # Input of the query (batch size x seq_len x d_k x d_v)
k1 = torch.randn(1024, 3, 64, 64)     # Input of the key (batch size x seq_len x d_k x d_v)
v1 = torch.randn(1024, 8, 512, 512)   # Input of the value (batch size x seq_len x d_v x d_v)
