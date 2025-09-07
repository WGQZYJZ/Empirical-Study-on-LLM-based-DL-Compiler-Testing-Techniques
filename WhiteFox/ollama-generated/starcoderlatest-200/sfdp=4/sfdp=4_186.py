
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_projection = torch.nn.Linear(512, 64)
        self.query_projection = torch.nn.Linear(512, 64)
 
    def forward(self, query, key, value, mask):
        # Apply a linear transformation to the input of shape (batch size, num heads, from seq length, dim per head).
        k  = self.key_projection(key)
        q  = self.query_projection(query)
        qk = torch.einsum("bcd, bcd -> cde", (q, k)) # This computes the dot-product of the query and key, and it is stored in qk
        attn_weights = torch.nn.functional.softmax(qk / math.sqrt(key.size(-1)), dim=-1)  # Scaled softmax function on the result

        output  = torch.einsum("cde, bcd -> cbe", (attn_weights, value)) # This computes attention weighted sum of the value
        attn_weights = None  # Freeing memory for reduced size and increased speed
        return output

class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention1 = Attention()
        self.attention2 = Attention()
 
    def forward(self, query, key, value, mask):
        v1  = self.attention1(query, key, value, mask)
        output = query + v1
        v2  = self.attention2(output, key, value, mask)
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        encoder_layer1 = TransformerEncoderLayer()
        encoder_layer2 = TransformerEncoderLayer()
 
        self.encoder_layer1 = torch.nn.Sequential(encoder_layer1, encoder_layer2)
 
    def forward(self, query, key, value, mask):
        return self.encoder_layer1(query, key, value, mask)

# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 512, 64, 64)  # batch size x seq length of q tensor
k  = torch.randn(1, 512, 64, 64)  # batch size x seq length of k tensor
v  = torch.randn(1, 512, 64, 64)  # batch size x seq length of v tensor
m_mask = torch.BoolTensor([[True] * 3 + [False]]).transpose(-1,-2) # (seq len, num heads, batch size) mask tensor
