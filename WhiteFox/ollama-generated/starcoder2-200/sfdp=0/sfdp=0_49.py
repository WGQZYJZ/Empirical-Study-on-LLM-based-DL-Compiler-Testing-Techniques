class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qry: torch.Tensor, ky: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
 
        inv_scale = 1 / math.sqrt(qry.size(-1))
        scaled_dot_product = torch.matmul(
            query=qry, key=ky.transpose(-2, -1)) / inv_scale 
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output = attention_weights.matmul(v) 
        return output
