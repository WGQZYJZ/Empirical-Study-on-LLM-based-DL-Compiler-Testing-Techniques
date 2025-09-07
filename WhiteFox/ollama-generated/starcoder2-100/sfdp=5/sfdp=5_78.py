
import torch
 
class Model(torch.nn.Module):
    def __init__(self, embedding=10):
        super().__init__()
        self._embedding = torch.nn.Embedding(32768, 4096)
        self._layernorm = torch.nn.LayerNorm(normalized_shape=[4096], eps=1e-6)
        self._dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, query):
        attn = torch.dot(query, torch.transpose(query, -2, -1)) / math.sqrt(
            torch.norm(query).pow(-2)
        )
        attn = self._dropout(attn)
        attn += torch.eye(attn.size(-1), device=attn.device)  # Add the identity matrix to the dot product
        attn_weight = torch.softmax(attn, dim=-1)
        output = torch.dot(attn_weight, query)  # Compute the dot product of the dropout output and the value
        return self._layernorm(self._embedding(output))


model = Model()
input = torch.rand(256, 4096)

output = model(input)