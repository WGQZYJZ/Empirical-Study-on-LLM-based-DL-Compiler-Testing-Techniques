
class Transformer(torch.nn.Module):
    def __init__(self, embedding_dim=512):
        super().__init__()
        self.embedding = torch.nn.Embedding(3, 8)
        self.linear   = torch.nn.Linear(8*8, embedding_dim)
 
    def forward(self, x1, x2):
        # input shape: [batch_size, seq_len]
        v = self.embedding(x1) 
        output  = (v.view(-1, 8 * 64) @ self.linear.weight.T) + self.linear.bias
        return output


# Initializing the model
m = Transformer()
 
# Inputs to the model
x1 = torch.randint(0, high=3, size=(20,)).to(torch.int64)
x2 = torch.randn(20, 3).to(torch.float32)
