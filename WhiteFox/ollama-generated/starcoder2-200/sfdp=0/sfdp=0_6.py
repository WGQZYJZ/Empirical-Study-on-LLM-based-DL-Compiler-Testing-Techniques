
class AttentionModel(torch.nn.Module):
    def __init__(self, query_size=1024, key_size=768):
        super().__init__()
        self._key = torch.randn((query_size, key_size))  # Query
        self._value = torch.randn((query_size, key_size))  # Value
 
        self._scale = query_size ** -0.5
 
    def forward(self, input):
        v1  = torch.matmul(input, self._key) / self._scale  # Scaled Dot-Product Attention
        v2  = v1.softmax(dim=-1)
        output  = v2 @ self._value
 
        return output


# Initializing the model