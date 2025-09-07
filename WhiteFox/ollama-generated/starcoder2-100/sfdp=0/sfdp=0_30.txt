
class DotProductAttention(torch.nn.Module):
    def __init__(self, d_model=1024, dropout=0.5, scale=False):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)

        # Initialize parameters for the scaled dot product attention mechanism
        self.scale  = (d_model ** -0.5) * int(scale is not False),

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        batch_size1, n1, dim1 = query.shape
        _, n2, dim2 = key.shape

        assert dim1 == self.d_model  and n1 * n2 % 8 is 0
        inv_scale = self.inv_scale if scale else None 
        scaled_dot_product  = torch.einsum('ijk,ilk->ijl', [query / inv_scale for q in query] * 3)
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        output  = attention_weights @ value
        return self.dropout(output)

m  = DotProductAttention()

