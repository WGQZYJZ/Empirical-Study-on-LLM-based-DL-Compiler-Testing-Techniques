

class AttentionModel(torch.nn.Module):
    def __init__(self, d_model: int = 768, qkv_scale: float = None):
        super().__init__()
        self.d_model = d_model
        self._qkv_scale = qkv_scale

        self.query_proj = torch.nn.Linear(
            in_features=self.d_model // 4 * 3, out_features=self.d_model)
        self.key_proj = torch.nn.Linear(in_features=self.d_model,
                                        out_features=self.d_model)

        self.scale_factor = self._get_scale_factor()

    def forward(self, query: torch.Tensor):
        value = query  # Get the query tensor.

        qk = torch.matmul(query, key.transpose(-2, -1)) / \
            math.sqrt(self.d_model // 4)
        scaled_qk = qk * scale_factor

        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.85)
        output = dropout_qk.matmul(value)

m  = AttentionModel()

 # Inputs to the model
    query = torch.randn(32, 768)

    __output__  = m(query)

