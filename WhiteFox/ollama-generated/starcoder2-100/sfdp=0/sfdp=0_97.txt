
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, embedding_dim=512, max_sequence_length = 4096):
        super().__init__()
        self.scale = torch.rsqrt(torch.tensor([embedding_dim]).to(device))
        self.softmax = nn.Softmax(dim=-1)
 
    def forward(self, query: TensorType, key: TensorType, value: TensorType) -> Tuple[TensorType]:
        attention_weights  = torch.matmul(query / self.scale, key.transpose(-2, -1)) 
        scaled_dot_product  = torch.nn.functional.softmax(attention_weights, dim=-1)
        output  = scaled_dot_product @ value
 
        return output


# Initializing the model
scaled_dot = ScaledDotProductAttention()


# Inputs to the model
query = torch.randn((2048))
key = torch.randn((32768, 512))
value = torch.randn((32768, 512))

__output__  = scaled_dot(query, key, value)
