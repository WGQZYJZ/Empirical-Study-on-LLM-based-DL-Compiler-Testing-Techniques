
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
            scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / sqrt(torch.tensor([query.shape[-1]], device=query.device).float())
            attention_weights = scaled_dot_product.softmax(dim=-1)
            output  = attention_weights.matmul(value)
            return output


# Initializing the model
m = AttentionModel()
 
# Inputs to the model, query, key and value tensors with shapes [N, H, W] for example [2048, 56, 56], [2048, 193, 193] and [2048, 2074] respectively
query = torch.randn(2048, 56, 56)
key   = torch.randn(2048, 193, 193)
value = torch.randn(2048, 2074)
