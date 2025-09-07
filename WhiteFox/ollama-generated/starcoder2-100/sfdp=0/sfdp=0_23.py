
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 100) -> None:
        super().__init__()

        self.scaled_dot_product = torch.nn.Linear(
            in_features=3 * 768, out_features=768
        )

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ):
        scaled_dot_product = self.scaled_dot_product(query @ key) / inv_scale

        attention_weights = scaled_dot_product.softmax(dim=-1)

        output = attention_weights @ value
        return output


# Initializing the model and setting the constant inversion scaling factor to 0.5.
scaled_attention_model  = ScaledDotProductAttention()
scaled_attention_model.scaled_dot_product.weight  = torch.nn.Parameter(torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float))
scaled_attention_model.scaled_dot_product.bias    = torch.nn.Parameter(torch.tensor([0], dtype=torch.float))


# Inputs to the model
query  = torch.randn(1,3,768)
key   = torch.randn(256,768)
value = torch.randn(256,3,768)

__output__  = scaled_attention_model(query, key, value)
