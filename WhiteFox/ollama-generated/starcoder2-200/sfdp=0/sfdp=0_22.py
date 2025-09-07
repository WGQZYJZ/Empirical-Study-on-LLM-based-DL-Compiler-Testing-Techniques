
class AttentionModel(torch.nn.Module):
    def __init__(self, dim=2048, num_heads=16):
        super().__init__()
        self._scale  = torch.sqrt(dim)
        self.wqv = torch.nn.Linear(in_features=dim, out_features=num_heads * dim // num_heads)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v1  = self.wqv(query).reshape(
            shape=[-1] + [
                int(self._scale)] + list(query.shape[-2:])
        )
 
        v2  = v1.softmax(dim=-3)
        return v2 @ value

# Initializing the model
m = AttentionModel()

 # Inputs to the model
query = torch.randn(size=[8, 64])
key = torch.randn(size=[8, 50729]).reshape([1] + [327] + list(torch.randn(size=[8, 1, 1]).shape[-2:]))
value = torch.randn(size=[8, 64])

 # Running the model with inputs
output = m(query=query, key=key, value=value)