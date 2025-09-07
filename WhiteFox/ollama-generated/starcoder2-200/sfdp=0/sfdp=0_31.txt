
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, embedding_size: int) -> None:
        super().__init__()
        self.scale = math.sqrt(embedding_size)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        attention_weights  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        return attention_weights


class TransformerBlock(torch.nn.Module):
    def __init__(self, embedding_size=768, nhead=4) -> None: 
        super().__init__()
 
        # Layer 1
        self.linear1 = torch.nn.Linear(embedding_size, embedding_size * 2)
        self.dropout1 = torch.nn.Dropout(0.5)
 
        # Layer 2
        self.linear2 = torch.nn.Linear(embedding_size * 2, embedding_size)
        self.dropout2 = torch.nn.Dropout(0.5)
 
        self.attn = ScaledDotProductAttention(embedding_size=768)
 
    def forward(self, x): 
        out1 = F.relu(self.linear1(x))
        out1 = self.dropout1(out1)
        out2 = self.attn(query=out1, key=out1, value=out1)
 
        out3 = F.relu(self.linear2(out1 + out2)) 
        return self.dropout2(out3 + out2)

m  = TransformerBlock()


# Initializing the model
m0  = m(torch.randn(4,8,768))

x0  = torch.randint(-50,51,(4,8,768))
x1  = x0 + 30
x2  = x0 - 10

